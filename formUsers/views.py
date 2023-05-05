from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import FormUserSerializer
from .models import FormUserModel


class CreateUserFormApiView(CreateAPIView):
    queryset = FormUserModel.objects.all()
    serializer_class = FormUserSerializer

    permission_classes = (AllowAny,)
