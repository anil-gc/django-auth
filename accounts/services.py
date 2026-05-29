from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from .utils import generate_otp
from .models import OTP
from decouple import config

User = get_user_model()

def send_otp_email(email):
    user = User.objects.get(email = email)
    otp_code = generate_otp()

    OTP.objects.create(
        user = user,
        code = otp_code
    )

    subject = "Password Reset OTP"
    message = f'your OTP code is {otp_code}'
    from_email = config('EMAIL_HOST_USER')
    recipient_list = [email]

    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False, # If False, Django will raise an error if the email fails to send
    )