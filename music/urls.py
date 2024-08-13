from django.urls import path
from music.views import index,show_news

urlpatterns = [
    path('', index, name='index'),
    path('show/news/<int:id>/', show_news, name='show_news'),
    
]