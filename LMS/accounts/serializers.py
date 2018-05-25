from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User


class CompositeUserSerializer(serializers.Serializer):
    """
    This serializer combines data from django auth user
    and user profile model
    """
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    last_login = serializers.DateTimeField(allow_null=True)
    date_joined = serializers.DateTimeField()


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)



class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the  User model in django auth
    """
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')


#
# class UserProfileSerializer(serializers.ModelSerializer):
#     """
#     Serializer for the User Profile model
#     """
#     class Meta:
#         model = UserProfile
#         fields = '__all__'

#
# from rest_framework import serializers
#
# from .models import User
# from .utils import email_validator
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('email', 'first_name', 'last_name',)
#
#
# class StudentRegistrationSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField()
#
#     class Meta:
#         model = User
#         fields = ('id', 'email', 'first_name', 'last_name', 'password')
#
#     def create(self, validated_data):
#         """
#         Create the object.
#
#         :param validated_data: string
#         """
#         user = User.objects.create(**validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
#
#     def validate_email(self, value):
#         """
#         Validate if email is valid or there is a user with the email.
#
#         :param value: string
#         :return: string
#         """
#
#         if not email_validator(value):
#             raise serializers.ValidationError('Please use a different email address provider.')
#
#         if User.objects.filter(email=value).exists():
#             raise serializers.ValidationError('Email already in use, please use a different email address.')
#
#         return value
