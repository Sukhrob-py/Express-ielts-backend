from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from mockexam.models import MockExamModel
from payme.models import MerchatTransactionsModel
from .models import LessonPaymentModel
from pyclick.models import ClickTransaction


class MockPaymentAPiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        mockexam = MockExamModel.objects.last()
        mock_payment = LessonPaymentModel.objects.filter(user=user)
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
