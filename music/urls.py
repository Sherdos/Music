from django.urls import path
from music.views import index

urlpatterns = [
    path('', index, name='index')
]