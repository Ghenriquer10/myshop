from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class CustomUser(AbstractBaseUser):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.email
