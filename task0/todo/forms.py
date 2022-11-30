from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

class apply(ModelForm):
    Category=forms.ChoiceField(choices=[('high','High'),('medium','Medium'),('low','Low')])
    class Meta:
        model = List
        fields = ['title','desc','Complete','Category']
        #fields = '__all__'

class userform(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','profile_pic']