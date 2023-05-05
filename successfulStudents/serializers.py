from rest_framework import serializers
from .models import IeltsStudentsModel


class IeltsSrudentsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = IeltsStudentsModel
