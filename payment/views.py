from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import GeneratePayLinkSerializer
from mock_payment.models import MockPaymentModel
from mockexam.models import MockExamModel
from lesson_payment.models import LessonPaymentModel
from lessons.models import LessonModel
from teachers.models import TeachersModel
from payme.methods.generate_link import GeneratePayLink
from payme.models import Order
from drf_yasg.utils import swagger_auto_schema


class GeneratePayLinkMockAPIView(APIView):
    @swagger_auto_schema(
        request_body=GeneratePayLinkSerializer,
        responses={200: "{'pay_link': str}"}
    )
    def post(self, request, *args, **kwargs):
        lastmock = MockExamModel.objects.last()
        neworder = Order.objects.create(amount=lastmock.cost)
        MockPaymentModel.objects.create(
            mockexam=lastmock, user=request.user, amount=lastmock.cost, order_id=neworder.id)
        datas = request.data
        print(datas)
        datas['order_id'] = neworder.id
        serializer = GeneratePayLinkSerializer(
            data=datas
        )
        serializer.is_valid(
            raise_exception=True
        )
        pay_link = GeneratePayLink(**serializer.validated_data).generate_link()

        return Response({"pay_link": pay_link})


class GeneratePayLinkLessonAPIView(APIView):
    @swagger_auto_schema(
        request_body=GeneratePayLinkSerializer,
        responses={200: "{'pay_link': str}"}
    )
    def post(self, request, *args, **kwargs):
        teacher_yuid = request.data['teacher']
        amount = request.data['amount']
        neworder = Order.objects.create(amount=amount)
        datas = request.data
        datas['order_id'] = neworder.id
        serializer = GeneratePayLinkSerializer(
            data=datas
        )
        teacher = TeachersModel.objects.get(yuid=teacher_yuid)
        LessonPaymentModel.objects.create(
            user=request.user, teacher=teacher, amount=float(amount/100), order_id=neworder.id)
        serializer.is_valid(
            raise_exception=True
        )
        pay_link = GeneratePayLink(**serializer.validated_data).generate_link()

        return Response({"pay_link": pay_link})
