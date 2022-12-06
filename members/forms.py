from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

FAMILY_CHOICES = (
("EBIYAU", "EBIYAU"),
("PORTER","PORTER")
)
class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60,widget=forms.PasswordInput)
    #family = forms.ChoiceField(choices=FAMILY_CHOICES)

class UploadForm(ModelForm):
    title = forms.CharField(max_length=60)
    text = forms.CharField(max_length=600)


    class Meta:
        model = Document
        fields = ['user','created_by','title','text']

class CreateUserForm(UserCreationForm):


    class Meta:
        model = User
        fields = ['username','password1','password2']


    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for field_name in ('username',  'password1', 'password2'):
            self.fields[field_name].help_text = ''
