from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from services.models import RevolvingDoor

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

class DeleteFORM(forms.Form):
     captcha = forms.IntegerField(label='İşlemi Doğrula :  5 + 0 = ? ')

     def clean(self):

        data = self.cleaned_data.get('captcha')
        if data:

            if data != 5:
                raise forms.ValidationError('Sonuç yanlış !')
        return super(DeleteFORM,self).clean()        

class UpdateMR30Form(forms.ModelForm):

    class Meta:
        model = RevolvingDoor

        fields = [
            'company',
            'adress',
            'delivery_method',
            'delivery_date',
            'mr30_type',
            'dia',
            'trans_height',
            'canopy',
            'wing',
            'fixed_glass',
            'moving_glass',
            'color',
            'lighting',
            'broken_wing',
            'ground_circle',
            'night_sensor',
            'heel_sensor',
            'hand_sensor',
            'spot_scan',
            'spain_key',
            'stain_arm',
            'button_pole',
            'notes',
            'drawing',
            'control',
            'manufacturing_chief',
        ]

