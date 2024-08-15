from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(
        self,
        email=None,
        nome=None,
        endereco=None,
        telefone=None,
        cpf=None,
        nascimento=None,
        password=None,
    ):
        if not email:
            raise ValueError("Usuários devem ter um email")

        user = self.model(
            email=self.normalize_email(email),
            nome=nome,
            endereco=endereco,
            telefone=telefone,
            cpf=cpf,
            nascimento=nascimento,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    nome = models.CharField(max_length=255, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    nascimento = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
