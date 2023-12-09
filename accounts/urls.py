from django.urls import path
from accounts.views import *

urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("register/", RegisterView.as_view(), name='register'),
    path("verify/", VerifyAPI.as_view(), name='verify'),
]