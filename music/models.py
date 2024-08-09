from django.db import models

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
        
    