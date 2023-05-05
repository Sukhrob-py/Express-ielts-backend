from rest_framework import serializers

from rest_framework.exceptions import ValidationError

from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  'email',
                  'password',
                  'yuid',
                  'created_at',
                  'updated_at'
                  )

    def create(self, validated_data):
        email = validated_data.get('email')
        username = validated_data.get('username')
        password = validated_data.get('password')
        isEmail = User.objects.filter(email=email)
        if isEmail.exists():
            raise ValidationError({
                'message': "This email is already exist!",
                'success': False
            })
        isUsername = User.objects.filter(username=username)
        if isUsername.exists():
            raise ValidationError({
                'message': "This username is already exist!",
                'success': False
            })
        elif len(username) < 5 and len(username) > 30:
            raise ValidationError({
                'message': "Username's length must be 5 to 30 characters",
                'success': False
            })
        elif username.isdigit() and not username.isdigit():
            raise ValidationError({
                'message': "Username must start with a letter (not number)",
                'success': False
            })
        elif username.isdigit():
            raise ValidationError({
                'message': "Username can not be a number",
                'success': False
            })

        if len(password) < 5:
            raise ValidationError({
                'message': "Password must be at least 5 charcters!",
                'success': False
            })
        elif password.isdigit() or password.isalpha():
            raise ValidationError({
                'message': "Password must contain letters and numbers"
            })

        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    def to_representation(self, instance):
        data = super(SignUpSerializer, self).to_representation(instance)
        data.update(instance.tokens())
        data.pop("password", None)
        return data
