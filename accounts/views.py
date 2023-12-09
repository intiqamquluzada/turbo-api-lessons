from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import LoginSerializer, RegisterSerializer, VerifySerializer
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.emails import send_otp_w_mail

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
        email = serializer.validated_data.get("email")
        user = User.objects.get(email=email)
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

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_otp_w_mail(serializer.data['email'])

        return Response(serializer.data, status=201)

# user.activate_code

# class VerifyAPI(APIView):
#     def post(self, request):
#         data = request.data
#         serializer = VerifySerializer(data=data)
#         if serializer.is_valid():
#             email = serializer.data['email']
#             otp = serializer.data['otp']
#             user = User.objects.get(email=email)  # get -> 1 eded, filter -> coxlu
#             # intiqam@gmail.com(huseynli), intiqam@gmail.com(Guluzade)
#             if not user:
#                 return Response({
#                     'status': 400,
#                     'message': 'something went wrong',
#                     'data': 'invalid email'
#                 })
#             if not user.activate_code == otp:
#                 return Response({
#                     "status": 400,
#                     "message": "something went wrong",
#                     'data': 'wrong otp'
#                 })
#             # user = user
#             user.is_active = True
#             user.save()
#             return Response({
#                 "status": 200,
#                 "message": "account verified",
#                 "data": user.email
#             })


class VerifyAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')
        if email and otp:
            try:
                user = User.objects.get(email=email, activate_code=otp)
                user.is_active = True
                user.save()
                return Response({'message': 'Email verified successfully.'}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'message': 'Invalid OTP or email.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Email and OTP are required.'}, status=status.HTTP_400_BAD_REQUEST)

