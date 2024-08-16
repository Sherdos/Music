from django.shortcuts import render, redirect
from music.models import Music, News
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from music.forms import NewsForm,RegisterForm, LoginForm

# Create your views here.


def index(request):
    form = LoginForm()
    music = Music.objects.latest('id')
    news = News.objects.all().order_by('-id')
    new_tracks = Music.objects.all().order_by('-date_pub')
    if request.GET.get('track'):
        id = request.GET.get('track')
        music = Music.objects.get(id=id)
    musics = Music.objects.all()
    context = {
        'music':music,
        'musics':musics,
        'news':news,
        'new_tracks':new_tracks,
        'form':form,
    }
    return render(request, 'index.html', context)


def show_news(request,id):
    news = News.objects.get(id=id)
    context = {
        'news':news
    }
    return render(request, 'show_news.html',context)




def user_register(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password1'])
            login(request,user)
    else:
        form = RegisterForm()
        
    return render(request, 'register.html', {'form':form})

def user_login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        user = authenticate(request, **form.cleaned_data)
        login(request,user)
    return redirect('index')

def test(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            News.objects.create(**data)
    else:
        form = NewsForm()
    return render(request, 'test.html',{'form':form})


def logout_user(request):
    logout(request)
    return redirect('index')