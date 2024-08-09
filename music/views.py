from django.shortcuts import render
from music.models import Music
# Create your views here.


def index(request):
    music = Music.objects.latest('id')
    return render(request, 'index.html', {'music':music})

