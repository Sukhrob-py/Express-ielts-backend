from django.urls import path
from .views import MockPaymentAPiView,MockPaymentOver
urlpatterns=[
    path("get/",MockPaymentAPiView.as_view()),
    path("over/",MockPaymentOver.as_view()),
]