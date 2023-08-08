from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUsuariosForm(UserCreationForm):
    username = forms.CharField(max_length=20, label="Usuario")
    first_name = forms.CharField(label="nombre")
    last_name = forms.CharField(label="apellido")
    email = forms.EmailField(label="Email Usuario")
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmar contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
        help_texts = {A: "" for A in fields}


class UsuarioEditForm(UserCreationForm):
    first_name = forms.CharField(label="nombre")
    last_name = forms.CharField(label="apellido")
    email = forms.EmailField(label="Email Usuario")
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmar contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
        help_texts = {A: "" for A in fields}


class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)
