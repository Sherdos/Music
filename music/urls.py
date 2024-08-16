from django.urls import path
from music.views import index,show_news,user_register, test, logout_user, user_login
    

urlpatterns = [
    path('', index, name='index'),
    path('show/news/<int:id>/', show_news, name='show_news'),
    path('user/register/', user_register, name='user_register'),
    path('user/login/', user_login, name='user_login'),
    path('test/', test, name='test'),
    path('logout/', logout_user, name='logout_user'),
    
]