from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from music.models import Music, News
from music.forms import NewsForm,CommentForm
from users.forms import LoginForm
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.


class IndexView(ListView):
    template_name =  'music/pages/index/index.html'
    model = Music
    context_object_name = 'musics'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        music = Music.objects.latest('id')
        if self.request.GET.get('track'):
            id = self.request.GET.get('track')
            music = Music.objects.get(id=id)
        context2 = {
            'title':'Главная',
            'music':music,
            'news':News.objects.all().order_by('-id'),
            'new_tracks':Music.objects.all().order_by('-date_pub'),
            'form_login': LoginForm(),
        }
        context.update(context2)
        return context
    

class DetailNewsView(DetailView,CreateView):
    template_name =  'music/pages/show_news/show_news.html'
    model = News
    context_object_name = 'news'
    form_class = CommentForm
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context2 = {
           'form_login': LoginForm(),
        }
        context.update(context2)
        return context
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.news = self.get_context_data()['news']
        comment.save()
        
      

def test(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            News.objects.create(**data)
    else:
        form = NewsForm()
    return render(request, 'music/pages/test.html',{'form':form})


class NewsListView(ListView):
    template_name = 'music/pages/news/news.html'
    model = News
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        return context
    

class TrackListView(ListView):
    template_name = 'music/pages/tracks/mp3s.html'
    model = Music
    context_object_name = 'tracks'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Треки'
        return context
    
class SearchView(ListView):
    
    template_name = 'music/pages/search.html'
    model = Music
    context_object_name = 'tracks'
    
    def get_queryset(self) -> QuerySet[Any]:
        key = self.request.GET.get('key')
        if key:
            return Music.objects.filter(title__icontains = key)
        return super().get_queryset()
    
    