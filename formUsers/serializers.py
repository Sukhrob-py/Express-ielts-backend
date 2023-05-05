from rest_framework import serializers

from .models import FormUserModel


class FormUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = FormUserModel
