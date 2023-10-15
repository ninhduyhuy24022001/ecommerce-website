from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

INPUT_FORM = 'w-full py-4 px-6 rounded-xl'

class SignupFrom(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your username",
        'class': INPUT_FORM
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your first name",
        'class': INPUT_FORM
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your last name",
        'class': INPUT_FORM
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': "Your email",
        'class': INPUT_FORM
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Your password",
        'class': INPUT_FORM
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Repeat passoword",
        'class': INPUT_FORM
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your username",
        'class': INPUT_FORM
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Your password",
        'class': INPUT_FORM
    }))