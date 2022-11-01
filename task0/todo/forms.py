from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class apply(ModelForm):
    Category=forms.ChoiceField(choices=[('high','High'),('medium','Medium'),('low','Low')])
    class Meta:
        model =List
        fields = ['title','desc','Complete','Category']

class userform(UserCreationForm):
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']