from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from .models import TeachersModel
from django.core.serializers import serialize
from rest_framework.response import Response
from .serializers import TeachersSerializer
from lessons.models import LessonModel
from lessonType.models import LessonType


class TeachersListApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        lesson_type = request.data.get('lesson_type')
        isLesson = LessonType.objects.filter(title=lesson_type)
        if not isLesson.exists():
            raise ValidationError({
                'message': "Something wrong ! Please try again later",
                'success': False
            })

        teachers = TeachersModel.objects.filter(lesson_type__title=lesson_type)
        serialized_teachers = serialize('json', teachers)

        return Response({
            'data': serialized_teachers
        })
