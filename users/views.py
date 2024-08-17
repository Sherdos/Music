from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.forms import LoginForm, RegisterForm

# Create your views here.

def user_register(request):
    form_login = LoginForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password1'])
            login(request,user)
    else:
        form = RegisterForm()
    
    context = {
        'form_login':form_login,
        'form':form,
    }
    return render(request, 'music/pages/register.html', context)

def user_login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        user = authenticate(request, **form.cleaned_data)
        login(request,user)
    return redirect('index')

def logout_user(request):
    logout(request)
    return redirect('index')
