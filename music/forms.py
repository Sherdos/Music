
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms



class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username','password1','password2')
        

