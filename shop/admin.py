from django.contrib import admin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    fields = (
        "email",
        "nome",
        "endereco",
        "telefone",
        "cpf",
        "nascimento",
        "is_active",
        "is_admin",
        "password",
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "nome",
                    "endereco",
                    "telefone",
                    "cpf",
                    "nascimento",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    list_display = (
        "email",
        "nome",
        "endereco",
        "telefone",
        "cpf",
        "nascimento",
        "is_active",
        "is_admin",
        "password",
    )
    search_fields = ("email", "nome", "cpf")
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
