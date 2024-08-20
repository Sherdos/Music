from django.urls import path
from music.views import IndexView,DetailNewsView, test,NewsListView,TrackListView, SearchView
    

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('show/news/<int:pk>/', DetailNewsView.as_view(), name='show_news'),
    path('test/', test, name='test'),
    path('news/', NewsListView.as_view(), name='news'),
    path('tracks/', TrackListView.as_view(), name='tracks'),
    path('search/', SearchView.as_view(), name='search'),
    
]