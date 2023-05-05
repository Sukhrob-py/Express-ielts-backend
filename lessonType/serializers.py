from rest_framework import serializers

from .models import LessonType


class LessonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonType
        fields = ('title', 'yuid')
