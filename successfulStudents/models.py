from django.db import models
from uuid import uuid4
# Create your models here.


class IeltsStudentsModel(models.Model):
    photo = models.ImageField(upload_to='ielts')
    yuid = models.UUIDField(editable=False, default=uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name
