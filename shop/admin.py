from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


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
    )
    search_fields = ("email", "nome", "cpf")
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
