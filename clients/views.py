from rest_framework.generics import ListAPIView
from rest_framework import permissions
from .models import ClientsVisaModel
from .serializers import ClientsVisaSerializer


class CientsVisaListApiView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = ClientsVisaModel.objects.all()
    serializer_class = ClientsVisaSerializer
