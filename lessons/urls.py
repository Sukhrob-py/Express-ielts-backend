from django.urls import path
from .views import LessonsListApiView


urlpatterns = [
    path('list/', LessonsListApiView.as_view(), name='lessons-list')
]
