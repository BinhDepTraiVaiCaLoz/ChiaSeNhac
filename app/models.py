from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your models here.
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']


class RegistrationForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        label='First Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Confirm Password'
    )