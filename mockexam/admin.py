from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(MockExamModel)
admin.site.register(MockExamListeningPhotoModel)
admin.site.register(MockExamListeningAudioModel)
admin.site.register(MockExamListeningAnswerModel)
admin.site.register(MockExamReadingAnswerModel)
admin.site.register(MockExamWritingModel)
admin.site.register(MockExamReadingPhotoModel)