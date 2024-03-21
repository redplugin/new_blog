from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    SUPERUSER, MODERATOR, APPUSER = 1, 2, 3

    ROLES = (
        (SUPERUSER, 'Superuser'),
        (MODERATOR, 'Moderator'),
        (APPUSER, 'AppUser'),
    )

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    role = models.IntegerField(default=APPUSER, choices=ROLES)

    date_joined = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []