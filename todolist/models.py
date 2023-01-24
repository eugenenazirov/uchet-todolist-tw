from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_("email_address"), unique=True, blank=True)
    phone_number = PhoneNumberField(max_length=30, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username
