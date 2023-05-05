from rest_framework import serializers

from .models import MockPaymentModel

class MockPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        fields=""