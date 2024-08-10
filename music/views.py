from django.shortcuts import render
from music.models import Music, News
# Create your views here.


def index(request):
    music = Music.objects.latest('id')
    news = News.objects.all().order_by('-id')
    if request.GET.get('track'):
        id = request.GET.get('track')
        music = Music.objects.get(id=id)
    musics = Music.objects.all()
    context = {
        'music':music,
        'musics':musics,
        'news':news
    }
    return render(request, 'index.html', context)

