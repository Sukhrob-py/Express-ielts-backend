from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from uuid import uuid4
# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    yuid = models.UUIDField(unique=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    purchased = models.BooleanField(default=False)
    cost = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }


class ResetPasswordModel(models.Model):
    code = models.CharField(max_length=6)
    email = models.EmailField()
    new_password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email} ---  {self.code} --- {self.status}"
