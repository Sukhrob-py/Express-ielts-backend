from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import permissions
from rest_framework.views import APIView
from django.core.serializers import serialize
from django.http import JsonResponse
from rest_framework.response import Response

from .models import FeedbackModel
from .serializers import FeesbackSerializer


class FeedbackCreateApiView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = FeedbackModel.objects.all()
    serializer_class = FeesbackSerializer

class FeedbackListApiView(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = FeedbackModel.objects.all()
    serializer_class = FeesbackSerializer
