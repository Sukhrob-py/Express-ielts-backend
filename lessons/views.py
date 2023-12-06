from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from django.core.serializers import serialize
from rest_framework.response import Response
from payme.models import MerchatTransactionsModel
from .models import LessonModel
from pyclick.models import ClickTransaction
from lesson_payment.models import LessonPaymentModel
from teachers.models import TeachersModel
from lessonType.models import LessonType


class LessonsListApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        teacher = request.data.get("teacher")
        lesson_type = request.data.get("lesson_type")
        isTeacher = TeachersModel.objects.filter(yuid=teacher)
        isLesson_type = LessonType.objects.filter(title=lesson_type)
        if (not isTeacher.exists() or not isLesson_type.exists()):
            raise ValidationError({
                'message': "Something wrong! Please try again later",
                'success': False
            })

        currentTeacher = TeachersModel.objects.get(yuid=teacher)
        user = request.user

        payments = LessonPaymentModel.objects.filter(
            teacher=currentTeacher, user=user)
        lessons = LessonModel.objects.filter(
            teacher__yuid=teacher, lesson_type__title=lesson_type)
        serialized_lessons = serialize("json", lessons)
        for i in payments:
            if MerchatTransactionsModel.objects.filter(order_id=i.order_id, state=2).exists() or ClickTransaction.objects.filter(id=i.order_id, status="confirmed"):
                return Response({
                    'data': serialized_lessons,
                    "message": "Paid",
                    "success": True
                })

        return Response({
            'data': serialized_lessons,
            "message": "not paid",
            "success": False
        })
