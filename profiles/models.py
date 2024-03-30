from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from profiles.managers import CustomUserManager


class Profile(AbstractBaseUser, PermissionsMixin):
    MAX_LENGTH_NAME = 30

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=MAX_LENGTH_NAME, blank=True)
    last_name = models.CharField(max_length=MAX_LENGTH_NAME, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email