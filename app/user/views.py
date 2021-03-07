from django.shortcuts import render
from user.serializers import UserSerializer
from rest_framework import generics


# Create your views here.

class CreateUserView(generics.CreateAPIView):
    # Create a new user in system
    serializer_class = UserSerializer
