from django.urls import path

from .views import IeltsListApiView

urlpatterns = [
    path('', IeltsListApiView.as_view(), name="ielts_students_list")
]
