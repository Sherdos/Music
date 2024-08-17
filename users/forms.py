from django import forms
from django.contrib.auth.models import User
  
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255, min_length=5, label='Логин')
    email = forms.EmailField(max_length=255,label='Почта')
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput,label='Пароль')
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput, label='Подверждение Пароля')
    
    
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return password2
    
    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username)
        if len(user) > 0:
            raise forms.ValidationError('Логин занять')
        return username
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, min_length=5, label='Логин')
    password = forms.CharField(max_length=255, widget=forms.PasswordInput,label='Пароль')

