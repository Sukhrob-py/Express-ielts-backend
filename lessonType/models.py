from django.db import models
from uuid import uuid4


class LessonType(models.Model):
    title = models.CharField(max_length=120, unique=True)
    yuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
