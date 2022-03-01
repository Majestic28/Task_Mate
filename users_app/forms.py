from dataclasses import fields
import email
from re import L
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# here we gonna make new customreg form, we ll inherit everything from USercreation form to custom reg form

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # if the field is mandatory then required = true

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]