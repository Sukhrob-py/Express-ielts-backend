from django.urls import path
from .views import CreateUserFormApiView

urlpatterns = [
    path('', CreateUserFormApiView.as_view())
]
