from rest_framework import serializers

from .models import *

class MockExamSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=MockExamModel
        
class MockExamReadingPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=MockExamReadingPhotoModel


class MockExamReadingAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=MockExamReadingAnswerModel

class MockExamListeningPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=MockExamListeningPhotoModel

class MockExamListeningAudioSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=MockExamListeningAudioModel

class MockExamListeningAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=MockExamListeningAnswerModel

class MockExamWritingSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=MockExamWritingModel
