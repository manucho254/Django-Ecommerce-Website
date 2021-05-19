from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class User_Register_Form(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1' ,'password2')
        permissions = ("home")