from rest_framework import generics
from django.shortcuts import render

from .models import Users, Stack
from .serializers import UserSerializer


class UserAPIView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
