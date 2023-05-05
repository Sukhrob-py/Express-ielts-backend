from rest_framework import serializers

from .models import TeachersModel


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachersModel
        fields = ('name', 'lesson_type', 'info', 'yuid', 'photo')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['lesson_type'] = instance.lesson_type.title
        return data
