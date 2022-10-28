from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class apply(ModelForm):
    class Meta:
        model =List
        fields = ['title','desc','Complete']

class userform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']