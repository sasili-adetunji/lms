from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the User Profile objects
    """
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')

        read_only_fields = (
            'created_on',
        )

        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'name': {'required': True},
            'email': {'required': True},
        }

    def create(self, validated_data):
        """
        Create and return a new user
        :param validated_data:
        :return:
        """
        user = UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
