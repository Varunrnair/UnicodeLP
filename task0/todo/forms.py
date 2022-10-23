from django import forms
from .models import *

class apply(forms.ModelForm):
    class Meta:
        model =List
        fields = '__all__'
