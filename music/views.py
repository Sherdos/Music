from django.shortcuts import render, redirect
from music.models import Music, News
from music.forms import NewsForm,CommentForm
from users.forms import LoginForm
from django.views.generic import ListView
# Create your views here.


def index(request):
    form_login = LoginForm()
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
        'form_login':form_login,
    }
    return render(request, 'music/pages/index/index.html', context)


def show_news(request,id):
    form_login = LoginForm()
    news = News.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.news = news
            comment.save()
    else:
        form = CommentForm()
    context = {
        'news':news,
        'form':form,
        'form_login':form_login
    }
    return render(request, 'music/pages/show_news/show_news.html',context)




def test(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            News.objects.create(**data)
    else:
        form = NewsForm()
    return render(request, 'music/pages/test.html',{'form':form})


class NewsListView(ListView):
    template_name = 'music/pages/news/news.html'
    model = News
    context_object_name = 'news'
    

class TrackListView(ListView):
    template_name = 'music/pages/tracks/mp3s.html'
    model = Music
    context_object_name = 'tracks'