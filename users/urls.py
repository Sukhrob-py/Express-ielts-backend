from django.urls import path

from .views import SignUpView, LoginApiView, ResetPasswordAPiView, ResetPasswordConfirmationApiView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', LoginApiView.as_view(), name="login"),
    path('reset-password/', ResetPasswordAPiView.as_view(), name="reset-password"),
    path('reset-password-confirm/', ResetPasswordConfirmationApiView.as_view(),
         name="reset-password-confirm"),
]
