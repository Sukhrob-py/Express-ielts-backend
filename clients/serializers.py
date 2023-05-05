from rest_framework import serializers

from .models import ClientsVisaModel


class ClientsVisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientsVisaModel
        fields = "__all__"
