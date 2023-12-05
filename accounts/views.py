from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from accounts.serializers import LoginSerializer, RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

"""
LOGIN --> password + email(username) --> check --> login(request, user) #MVC
LOGIN --> password + email(username) --> generate 2 tokens : 1.Refresh,  2. Access
frontendDev->tokeni hara lazimdirsa yerlesdirir.
"""


class LoginView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get("username")
        user = User.objects.get(username=username)
        token = RefreshToken.for_user(user)

        # User daxil olub sisteme - username: intiqam

        data = {
            **serializer.data,
            "refresh": str(token),
            "access": str(token.access_token)

        }

        return Response(data, status=201)


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=201)
