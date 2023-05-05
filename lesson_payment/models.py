from django.db import models
from users.models import User
from lessons.models import LessonModel
from teachers.models import TeachersModel
from uuid import uuid4
# Create your models here.


class LessonPaymentModel(models.Model):
    amount = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeachersModel, on_delete=models.CASCADE)
    order_id = models.BigIntegerField()
    isPaid=models.BooleanField(default=False)
    perform_time = models.CharField(max_length=255,null=True,blank=True)
    cancel_time = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    yuid = models.UUIDField(default=uuid4, editable=False, unique=True)

    def __str__(self):
        return self.user.username + " "+self.amount+" "+self.teacher.__str__()


class Order(models.Model):
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    yuid = models.UUIDField(default=uuid4, editable=False, unique=True)
