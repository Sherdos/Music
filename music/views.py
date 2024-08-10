from django.shortcuts import render
from music.models import Music
# Create your views here.


def index(request):
    music = Music.objects.latest('id')
    if request.GET.get('track'):
        id = request.GET.get('track')
        music = Music.objects.get(id=id)
    musics = Music.objects.all()
    context = {
        'music':music,
        'musics':musics
    }
    return render(request, 'index.html', context)

