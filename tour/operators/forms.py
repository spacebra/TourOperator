from django import forms
from django.contrib.auth import authenticate

from operators.models import Operator

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
