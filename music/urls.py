from django.urls import path
from music.views import index,show_news, test,NewsListView,TrackListView
    

urlpatterns = [
    path('', index, name='index'),
    path('show/news/<int:id>/', show_news, name='show_news'),
    path('test/', test, name='test'),
    path('news/', NewsListView.as_view(), name='news'),
    path('tracks/', TrackListView.as_view(), name='tracks'),
    
]