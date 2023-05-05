from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from mockexam.models import MockExamModel
from .models import MockPaymentModel
from payme.models import MerchatTransactionsModel
from pyclick.models import ClickTransaction


class MockPaymentAPiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        mockexam = MockExamModel.objects.last()
        mock_payment = MockPaymentModel.objects.filter(
            mockexam=mockexam, user=user)
        # print(mock_payment.order_id)
        for i in mock_payment:
            if MerchatTransactionsModel.objects.filter(order_id=i.order_id, state=2).exists() or ClickTransaction.objects.filter(id=i.order_id, status="confirmed").exists():
                return Response({
                    "message": "Paid",
                    "success": True
                })

        return Response({
            "message": "not Paid",
            "success": False
        })


class MockPaymentOver(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        mockexam = MockExamModel.objects.last()
        mock_payment = MockPaymentModel.objects.filter(
            mockexam=mockexam, user=user, isOver=False)
        # mock_payment.isOver=True
        for i in mock_payment:
            i.isOver = True
            i.save()

        return Response({
            "success": True
        })
