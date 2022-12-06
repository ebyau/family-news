from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class UploadForm(ModelForm):
    message = forms.FileField(label="Transcription File")
    file = forms.FileField(label="Audio File")

    class Meta:
        model = Audio
        fields = ['user','message','file']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60,widget=forms.PasswordInput)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for field_name in ('username',  'password1', 'password2'):
            self.fields[field_name].help_text = ''
