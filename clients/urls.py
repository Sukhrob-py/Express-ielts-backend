from django.urls import path
from .views import CientsVisaListApiView

urlpatterns = [
    path('', CientsVisaListApiView.as_view(), name="clients_visa")
]
