from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(max_length=30, unique=True)

    def __str__(self):
        return self.username
