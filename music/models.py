from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Music(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    discription = models.TextField(verbose_name='описание')
    date_pub = models.DateField(verbose_name='дата пубикации')
    file = models.FileField(verbose_name='файл', upload_to='music/')
    
    def __str__(self) -> str:
        return f'{self.title}'
    
    
    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыки'
        

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    text = models.TextField(verbose_name='описание')
    image = models.ImageField(verbose_name='фото',upload_to='new/')
    created = models.DateTimeField(verbose_name='дата', auto_now_add=True)
    
    def __str__(self):
        return f'Название: {self.title}, Дата: {self.created}'
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        
        
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    news = models.ForeignKey('music.News', on_delete=models.CASCADE, verbose_name='Новость')
    text = models.TextField(verbose_name='текст')
    date = models.DateTimeField(verbose_name='дата', auto_now_add=True)
    
    def __str__(self):
        return f'пользователь: {self.user}, Дата: {self.date}'
    
    
    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'