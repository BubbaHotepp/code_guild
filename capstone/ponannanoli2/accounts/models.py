from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    username = models.CharField(_('username'), max_length=50, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class User_flag(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    USER_TYPE = [
        ('Staff', 'Staff'),
        ('User', 'User'),
    ]
    user_type = models.CharField(max_length=50, choices=USER_TYPE, blank=True, null=True)

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpb', upload_to='_profile_pics')
    location = models.CharField(max_length=50, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=CustomUserManager)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
    