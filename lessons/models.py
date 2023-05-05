from django.db import models
from teachers.models import TeachersModel
# Create your models here.
from uuid import uuid4
from lessonType.models import LessonType


class LessonModel(models.Model):
    teacher = models.ForeignKey(TeachersModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    lesson_type = models.ForeignKey(LessonType, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos')
    yuid = models.UUIDField(default=uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "...   " + self.teacher.name + "...   "+self.lesson_type.title
