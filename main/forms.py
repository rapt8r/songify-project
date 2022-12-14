from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
import django.forms.widgets as widgets


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password'}),
        required=True,
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password'}),
        required=True,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'}, ),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'username': {
                'unique': 'This username exists!',
                'required': 'Enter username!'
            },
            'password2': {
                'password_mismatch': 'Passwords are not identical!',
            },
            'email': {
                'unique': 'Ten adres email jest już używany!'
            }

        }


class AuthForm(AuthenticationForm):
    username = forms.CharField(
        widget=widgets.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter username'}))
    password = forms.CharField(
        widget=widgets.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter password'}))
