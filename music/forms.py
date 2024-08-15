from django import forms


class NewsForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    image = forms.FileField()
    
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255, min_length=5)
    email = forms.EmailField(max_length=255)
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput)
    
