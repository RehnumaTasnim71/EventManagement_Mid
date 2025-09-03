from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .utils import send_activation_email

@receiver(post_save, sender=User)
def on_user_created_send_activation(sender, instance, created, **kwargs):
    if created and not instance.is_active and instance.email:
        request = None  
        send_activation_email(instance, request)
