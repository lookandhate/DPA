from django.shortcuts import render
from rest_framework import viewsets

from common.views import MultiSerializerMixin
from user.api.serializers import UserSerializer, CreateUserSerializer
from user.models import User


# Create your views here.


class UserViewSet(MultiSerializerMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    default_serializer_class = UserSerializer
    serializer_classes = {"create": CreateUserSerializer}
