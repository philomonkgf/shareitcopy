from django.conf import settings
from django.core.mail import send_mail


# https://web-production-b85e0.up.railway.app/image_post/user_signin/

def send_email_verify(email,token):
    subject = 'You Accout needs to verified'
    message = f'Click on the link to Verify https://web-production-b85e0.up.railway.app/image_post/email_verify/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    
    send_mail(subject,message,email_from,recipient_list)
    
    
def send_reset_password(email,token):
    subject = 'Password Reset '
    message = f'Click on the link to reset The password https://web-production-b85e0.up.railway.app/image_post/password_verify/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    
    send_mail(subject,message,email_from,recipient_list)