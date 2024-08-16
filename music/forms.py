from django import forms


class NewsForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    image = forms.FileField()
    
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255, min_length=5, label='Логин')
    email = forms.EmailField(max_length=255,label='Почта')
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput,label='Пароль')
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput, label='Подверждение Пароля')
    
    
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return password2
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, min_length=5, label='Логин')
    password = forms.CharField(max_length=255, widget=forms.PasswordInput,label='Пароль')

