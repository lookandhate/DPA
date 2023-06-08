from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password", "is_superuser", "is_staff")


class CreateUserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    is_created = serializers.BooleanField(default=False, read_only=True)

    class Meta:
        model = User
        fields = ("id", "phone", "is_created", "password")

    def to_representation(self, instance):
        return UserSerializer().to_representation(instance)
