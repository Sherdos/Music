from django.shortcuts import render
from music.models import Music, News
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
