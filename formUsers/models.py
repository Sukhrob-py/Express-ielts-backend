from django.db import models
from uuid import uuid4
# Create your models here.


class FormUserModel(models.Model):
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"
