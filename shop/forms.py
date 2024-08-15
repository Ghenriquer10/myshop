from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit
from django import forms

from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ("nome", "endereco", "telefone", "cpf", "email", "nascimento")
        widgets = {
            "telefone": forms.TextInput(
                attrs={"type": "tel", "pattern": "[0-9]{10,15}"}
            ),
            "cpf": forms.TextInput(attrs={"pattern": "[0-9]{11}"}),
            "email": forms.EmailInput(),
            "nascimento": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("nome", css_class="form-control"),
            Field("endereco", css_class="form-control"),
            Field("telefone", css_class="form-control"),
            Field("cpf", css_class="form-control"),
            Field("email", css_class="form-control"),
            Field("nascimento", css_class="form-control"),
            Field("password1", css_class="form-control"),
            Field("password2", css_class="form-control"),
            Submit("submit", "Register", css_class="btn btn-primary"),
        )


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email", "nome", "endereco", "telefone", "cpf", "nascimento")
        widgets = {
            "telefone": forms.TextInput(
                attrs={"type": "tel", "pattern": "[0-9]{10,15}"}
            ),
            "cpf": forms.TextInput(attrs={"pattern": "[0-9]{11}"}),
            "email": forms.EmailInput(),
            "nascimento": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("nome", css_class="form-control"),
            Field("endereco", css_class="form-control"),
            Field("telefone", css_class="form-control"),
            Field("cpf", css_class="form-control"),
            Field("email", css_class="form-control"),
            Field("nascimento", css_class="form-control"),
            Submit("submit", "Save Changes", css_class="btn btn-primary"),
        )


class CustomUserLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("email", css_class="form-control"),
            Field("password", css_class="form-control"),
            Submit("submit", "Login", css_class="btn btn-primary"),
        )
