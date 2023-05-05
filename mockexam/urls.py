from django.urls import path

from .views import MockExamListeningApiView,MockExamReadingApiView,MockExamWritingApiView,MockExamSpeakingApiView,MockExamApiView

urlpatterns=[
    path('listening/',MockExamListeningApiView.as_view()),
    path('reading/',MockExamReadingApiView.as_view()),
    path('writing/',MockExamWritingApiView.as_view()),
    path('speaking/',MockExamSpeakingApiView.as_view()),
    path('get/',MockExamApiView.as_view()),
]