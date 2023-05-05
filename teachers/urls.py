from django.urls import path
from .views import TeachersListApiView
urlpatterns = [
    path('list/', TeachersListApiView.as_view(), name='teachers-list')
]
