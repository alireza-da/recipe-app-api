from django.shortcuts import render
from user.serializers import UserSerializer, AuthTokenSerializer
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


# Create your views here.


class CreateUserView(generics.CreateAPIView):
    # Create a new user in system
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    # Create a new auth token for user
    print("sere")
    serializer_class = AuthTokenSerializer
    print("sere")
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    # Manage the authenticated user
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
