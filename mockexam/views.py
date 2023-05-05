from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.serializers import serialize


import requests
from .serializers import *
from .models import *
from .models import MockExamModel as MockexamModel
TOKEN = "6276501921:AAHmLbjOm6V8IzXPtjeD38IIMZROdMOaIu4"
chat_id = "1079164955"
class MockExamApiView(APIView):
    permission_classes=(IsAuthenticated,)
    
    def get(self,request):
        data=MockexamModel.objects.last()
        return Response({
            "cost":data.cost,
            "yuid":data.yuid,
            "title":data.title
        })

class MockExamListeningApiView(APIView):
    permission_classes=(IsAuthenticated,)
    
    def get(self,request):
        mockexam=MockExamModel.objects.last()
        photos=MockExamListeningPhotoModel.objects.filter(mockexam=mockexam)
        audio=MockExamListeningAudioModel.objects.filter(mockexam=mockexam)
        answer=MockExamListeningAnswerModel.objects.filter(mockexam=mockexam)

        return Response({
            'photos':serialize("json",photos),
            'audio':serialize("json",audio),
            'answer':serialize("json",answer)
        })
    

class MockExamReadingApiView(APIView):
    permission_classes=(IsAuthenticated,)
    
    def get(self,request):
        mockexam=MockExamModel.objects.last()
        photos=MockExamReadingPhotoModel.objects.filter(mockexam=mockexam)
        answer=MockExamReadingAnswerModel.objects.filter(mockexam=mockexam)

        return Response({
            'photos':serialize("json",photos),
            'answer':serialize("json",answer)
        })

class MockExamWritingApiView(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        mockexam=MockExamModel.objects.last()
        photos=MockExamWritingModel.objects.filter(mockexam=mockexam)

        return Response({
            'photos':serialize("json",photos)
        })
    
    def post(self,request):
        message = request.data.get("message")
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json()) # this sends the message

        return Response({
            "message":"xabar yuborildi"
        })
    
class MockExamSpeakingApiView(APIView):
    
    permission_classes=(IsAuthenticated,)

    def post(self,request):
        
        message = request.data.get("message")
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json()) # this sends the message

        return Response({
            "message":"xabar yuborildi"
        })
