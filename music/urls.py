from django.urls import path
from music.views import index,show_news,user_register, test

urlpatterns = [
    path('', index, name='index'),
    path('show/news/<int:id>/', show_news, name='show_news'),
    path('user/register/', user_register, name='user_register'),
    path('test/', test, name='test'),
    
]