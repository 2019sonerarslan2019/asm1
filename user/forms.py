from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField

class LoginForm(forms.Form):

    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput())
    captcha = ReCaptchaField()

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username and password:

            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("Kullanıcı adı veya parola hatalı!")

        return super(LoginForm, self).clean()

