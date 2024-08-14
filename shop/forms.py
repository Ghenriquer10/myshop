from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ("nome", "endereco", "telefone", "cpf", "email", "nascimento")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("nome", css_class="form-control"),
            Field("endereco", css_class="form-control"),
            Field(
                "telefone",
                css_class="form-control",
                widget=forms.TextInput(
                    attrs={"type": "tel", "pattern": "[0-9]{10,15}"}
                ),  # Aceita números com 10 a 15 dígitos
            ),
            Field(
                "cpf",
                css_class="form-control",
                widget=forms.TextInput(attrs={"pattern": "[0-9]{11}"}),
            ),  # Aceita CPF com 11 dígitos
            Field("email", css_class="form-control", widget=forms.EmailInput()),
            Field(
                "nascimento",
                css_class="form-control",
                widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
            ),
            Field("password1", css_class="form-control"),
            Field("password2", css_class="form-control"),
            Submit("submit", "Register", css_class="btn btn-primary"),
        )


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email", "nome", "endereco", "telefone", "cpf", "nascimento")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("nome", css_class="form-control"),
            Field("endereco", css_class="form-control"),
            Field(
                "telefone",
                css_class="form-control",
                widget=forms.TextInput(
                    attrs={"type": "tel", "pattern": "[0-9]{10,15}"}
                ),  # Aceita números com 10 a 15 dígitos
            ),
            Field(
                "cpf",
                css_class="form-control",
                widget=forms.TextInput(attrs={"pattern": "[0-9]{11}"}),
            ),  # Aceita CPF com 11 dígitos
            Field("email", css_class="form-control", widget=forms.EmailInput()),
            Field(
                "nascimento",
                css_class="form-control",
                widget=forms.DateInput(attrs={"type": "date"}),
            ),
            Submit("submit", "Save Changes", css_class="btn btn-primary"),
        )
