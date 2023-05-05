from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from . import serializers
from .methods_merchant_api import Services
from .models import ClickTransaction
from .status import (ORDER_FOUND, INVALID_AMOUNT, ORDER_NOT_FOUND)
from .utils import PyClickMerchantAPIView
from mock_payment.models import MockPaymentModel
from mockexam.models import MockExamModel
from teachers.models import TeachersModel
from lesson_payment.models import LessonPaymentModel


class CreateClickTransactionView(CreateAPIView):
    serializer_class = serializers.ClickTransactionSerializer

    def post(self, request, *args, **kwargs):
        lastmock = MockExamModel.objects.last()
        amount = request.data.get('amount')
        order = ClickTransaction.objects.create(amount=amount)
        return_url = 'https://expressielts.uz/'
        if request.data['teacher']:
            teacher_yuid = request.data['teacher']
            print(teacher_yuid)
            teacher = TeachersModel.objects.get(yuid=teacher_yuid)
            LessonPaymentModel.objects.create(user=request.user, teacher=teacher, amount=float(
                amount), order_id=order.id)
        else:
            MockPaymentModel.objects.create(
                mockexam=lastmock, user=request.user, amount=lastmock.cost, order_id=order.id)
        url = PyClickMerchantAPIView.generate_url(
            order_id=order.id, amount=str(amount), return_url=return_url)
        return JsonResponse(url, safe=False)


class TransactionCheck(PyClickMerchantAPIView):
    @classmethod
    def check_order(cls, order_id: str, amount: str):
        if order_id:
            try:
                order = ClickTransaction.objects.get(id=order_id)
                if int(amount) == order.amount:
                    return ORDER_FOUND
                else:
                    return INVALID_AMOUNT
            except ClickTransaction.DoesNotExist:
                return ORDER_NOT_FOUND

    @classmethod
    def successfully_payment(cls, transaction: ClickTransaction):
        """ Эта функция вызывается после успешной оплаты """
        pass


class ClickTransactionTestView(PyClickMerchantAPIView):
    VALIDATE_CLASS = TransactionCheck


class ClickMerchantServiceView(APIView):
    def post(self, request, service_type, *args, **kwargs):
        service = Services(request.POST, service_type)
        response = service.api()
        return JsonResponse(response)
