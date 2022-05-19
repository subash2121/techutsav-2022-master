
import email
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings

def encrypt(pas):
    try:        
        pas = str(pas)
        cipher_pass = Fernet(settings.ENCRYPT_KEY)
        encrypt_pass = cipher_pass.encrypt(pas.encode('ascii'))
        encrypt_pass = base64.urlsafe_b64encode(encrypt_pass).decode("ascii") 
        return encrypt_pass
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None

@receiver(post_save,sender=User)
def send_welcome_email(sender,instance,created,**kwargs):
    if created and instance.email:
        body=render_to_string(
            'welcome_email_template.html',
            {
                'username':instance.username,
                'email':encrypt(instance.email)
            }
        )
        send_mail(
            'Welcome to TECHUTSAV @TCE',
            body,
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently=False,
            html_message=body
            )