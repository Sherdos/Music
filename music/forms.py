from django import forms
from django.contrib.auth.models import User
from music.models import Comment

class NewsForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    image = forms.FileField()
  
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)