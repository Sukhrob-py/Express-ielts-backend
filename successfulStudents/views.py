from rest_framework.generics import ListAPIView
from rest_framework import permissions

from .models import IeltsStudentsModel
from .serializers import IeltsSrudentsSerializer


class IeltsListApiView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = IeltsStudentsModel.objects.all()
    serializer_class = IeltsSrudentsSerializer
