from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']





class AuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Nazwa użytkownika'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Hasło'}))
