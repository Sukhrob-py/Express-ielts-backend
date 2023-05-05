from django.db import models
from lessonType.models import LessonType
# Create your models here.
from uuid import uuid4


class TeachersModel(models.Model):
    lesson_type = models.ForeignKey(
        LessonType, on_delete=models.CASCADE, related_name='teacher_lesson_type')
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=50)
    university = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    experience = models.CharField(max_length=50)
    yuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    photo = models.ImageField(upload_to='teachers/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
