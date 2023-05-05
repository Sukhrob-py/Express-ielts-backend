from django.db import models
from uuid import uuid4
# Create your models here.


class FeedbackModel(models.Model):
    owner = models.ForeignKey('users.User', models.Case, 'feedbacks')
    text = models.TextField()
    yuid = models.UUIDField(default=uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner.username
