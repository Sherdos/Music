from django.shortcuts import render, redirect
from music.models import Music, News
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from music.forms import RegisterForm

# Create your views here.


def index(request):
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
    }
    return render(request, 'index.html', context)


def show_news(request,id):
    news = News.objects.get(id=id)
    context = {
        'news':news
    }
    return render(request, 'show_news.html',context)




def user_register(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    if len(password) >= 8:
        try:
            User.objects.get(username = username)
        except:
            user = User.objects.create_user(username=username,email=email, password=password)
            login(request,user)
            return redirect('index')
    return redirect('index')

def test(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        image = request.FILES.get('image')
        
        News.objects.create(title = title, text=text, image=image)
        
    return render(request, 'test.html')

    