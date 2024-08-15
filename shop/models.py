from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(
        self, email, nome, endereco, telefone, cpf, nascimento, password=None
    ):
        if not email:
            raise ValueError("O usuário deve ter um endereço de e-mail")
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

    def create_superuser(
        self, email, nome, endereco, telefone, cpf, nascimento, password=None
    ):
        user = self.create_user(
            email,
            nome=nome,
            endereco=endereco,
            telefone=telefone,
            cpf=cpf,
            nascimento=nascimento,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14)
    email = models.EmailField(max_length=255, unique=True)
    nascimento = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome", "endereco", "telefone", "cpf", "nascimento"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
