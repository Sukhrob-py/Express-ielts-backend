from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from datetime import datetime
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
import random
from .models import User, ResetPasswordModel
from .serializers import SignUpSerializer
from django.core.mail import send_mail
import mailtrap as mt
import smtplib
import ssl


def send_email(to_email, code):

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "sukhrobovlayev@gmail.com"  # Enter your address
    receiver_email = to_email
    password = "rxqrjizcncmgdnmr"
    message = str(code)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


class SignUpView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    model = User
    serializer_class = SignUpSerializer


class LoginApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            raise ValidationError({
                "message": "username is incorrect!",
                "success": False
            })

        if user and check_password(password, user.password):
            return Response(
                data={
                    'success': True,
                    'access': user.tokens()['access'],
                    'refresh': user.tokens()['refresh'],
                    'username': user.username,
                    'email': user.email,
                }, status=200
            )
        else:
            raise ValidationError({
                "message": "password is incorrect!",
                "success": False
            })


class ResetPasswordAPiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        new_password = request.data.get('new_password')
        code = random.randint(100000, 1000000)
        ResetPasswordModel.objects.create(
            code=code, email=email, new_password=new_password)
        send_email(email, code)
        return Response({
            "message": "code has been sent!"
        })


class ResetPasswordConfirmationApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        code = request.data.get('code')

        confirmation = ResetPasswordModel.objects.filter(
            email=email, code=code, status=False)

        if confirmation.exists():
            try:
                user = User.objects.get(email=email)
            except:
                return Response({
                    "message": "this email is invalid"
                })
            user.set_password(confirmation[0].new_password)
            user.save()
            for i in confirmation:
                i.status = True
                i.save()
            return Response({
                "message": "password changed successfuly!"
            })
        return Response({
            "message": "code is invalid"
        })
