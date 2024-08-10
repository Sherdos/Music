from django.contrib import admin
from music.models import Music, News
# Register your models here.

class AdminMusic(admin.ModelAdmin):
    list_display = ('id','title', 'date_pub')
    search_fields = ('title',)
    list_filter = ('date_pub',)
    


admin.site.register(News)
admin.site.register(Music,AdminMusic)
