from django.core.mail import send_mail
from django.conf import settings
import random
from accounts.models import MyUser


def send_otp_w_mail(email):
    subject = 'Your account verfication email'
    otp = random.randint(1000, 9999)
    message = f'Your otp is {otp}'
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [email])
    user_obj = MyUser.objects.get(email=email)
    user_obj.activate_code = otp
    user_obj.save()
