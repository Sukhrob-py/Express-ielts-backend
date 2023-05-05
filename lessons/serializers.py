from rest_framework import serializers

from .models import LessonModel


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonModel
        fields = '__all__'
