from django.db import models
from django.contrib.auth.models import User

from music.models import Music
# Create your models here.

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='пользователь', related_name='profile')
    my_tracks_list = models.ManyToManyField(Music, verbose_name='Мои треки', blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профильи'
        
    def __str__(self) -> str:
        return f'Профиль {self.user}'
    
    


