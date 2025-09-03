from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

def user_profile_path(instance, filename):
    # uploaded files stored in media/profile_pics/<username>/<filename>
    return f'profile_pics/{instance.username}/{filename}'

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(
        upload_to=user_profile_path,
        default='profile_pics/default.png',
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )],
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username
