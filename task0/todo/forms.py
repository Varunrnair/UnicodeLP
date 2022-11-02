from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

class apply(ModelForm):
    Category=forms.ChoiceField(choices=[('high','High'),('medium','Medium'),('low','Low')])
    class Meta:
        model =List
        fields = ['title','desc','Complete','Category']

class userform(UserCreationForm):
    class Meta:
        model=User
        fields=['user_name','first_name','last_name','email','password1','password2']