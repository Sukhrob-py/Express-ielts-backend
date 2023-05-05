from django.urls import path

from .views import GeneratePayLinkMockAPIView,GeneratePayLinkLessonAPIView


urlpatterns = [
    path('pay-link-mock/', GeneratePayLinkMockAPIView.as_view(), name='generate-pay-link-mock'),
    path('pay-link-lesson/', GeneratePayLinkLessonAPIView.as_view(), name='generate-pay-link-lesson'),
]
