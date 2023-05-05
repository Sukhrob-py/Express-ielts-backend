from mockexam.models import MockExamModel
from users.models import User
from django.db import models
from uuid import uuid4

class MockPaymentModel(models.Model):
    mockexam=models.ForeignKey(MockExamModel,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.CharField(max_length=255)
    isPaid=models.BooleanField(default=False)
    order_id=models.IntegerField()
    isOver=models.BooleanField(default=False)
    yuid=models.UUIDField(default=uuid4,editable=False,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.__str__()