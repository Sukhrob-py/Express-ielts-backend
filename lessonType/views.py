from rest_framework.generics import ListAPIView
from rest_framework import permissions

from .models import LessonType
from .serializers import LessonTypeSerializer


class LessonTypeApiListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = LessonType.objects.all()
    serializer_class = LessonTypeSerializer
