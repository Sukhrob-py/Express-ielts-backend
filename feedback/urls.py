from django.urls import path

from .views import FeedbackCreateApiView, FeedbackListApiView

urlpatterns = [
    path('create/', FeedbackCreateApiView.as_view(), name='feedback_create'),
    path('list/', FeedbackListApiView.as_view(), name='feedback_list')
]
