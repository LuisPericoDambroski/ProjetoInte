from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    username = forms.CharField(max_length=100, label="Nome de Usuário")
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Senha")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirmar Senha")

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Email ou Nome de Usuário")
    password = forms.CharField(widget=forms.PasswordInput(), label="Senha")
        