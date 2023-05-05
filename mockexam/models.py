from django.db import models
from uuid import uuid4
# Create your models here.

class MockExamModel(models.Model):
    title=models.CharField(max_length=125,default="mock exam")
    yuid=models.UUIDField(default=uuid4,editable=False,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    cost=models.FloatField()

    def __str__(self):
        return self.title

class MockExamListeningPhotoModel(models.Model):
    mockexam=models.ForeignKey(MockExamModel,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="mock/listening")
    yuid=models.UUIDField(default=uuid4,editable=False,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mockexam.__str__()

class MockExamListeningAudioModel(models.Model):
    mockexam=models.ForeignKey(MockExamModel,on_delete=models.CASCADE)
    audio=models.FileField(upload_to="mock/listening")
    yuid=models.UUIDField(default=uuid4,editable=False,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mockexam.__str__()

class MockExamListeningAnswerModel(models.Model):
    mockexam=models.ForeignKey(MockExamModel,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="mock/listening")
    yuid=models.UUIDField(default=uuid4,editable=False,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mockexam.__str__()

class MockExamReadingPhotoModel(models.Model):
    mockexam=models.ForeignKey(MockExamModel,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="mock/reading")
    yuid=models.UUIDField(default=uuid4,editable=False,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mockexam.__str__()

class MockExamReadingAnswerModel(models.Model):
    mockexam=models.ForeignKey(MockExamModel,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="mock/reading")
    yuid=models.UUIDField(default=uuid4,editable=False,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mockexam.__str__()


class MockExamWritingModel(models.Model):
    mockexam=models.ForeignKey(MockExamModel,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="mock/writing")
    yuid=models.UUIDField(default=uuid4,editable=False,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mockexam.__str__()

# class MockExamSpeakingModel(models.Model):
#     mockexam=models.ForeignKey(MockExamModel,on_delete=models.CASCADE)
#     date=models.CharField(max_length=255)
#     yuid=models.UUIDField(default=uuid4,editable=False,unique=True)
#     created_at=models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.mockexam.__str__()

    

