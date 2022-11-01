from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class List(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField(max_length=200 ,default="")
    Complete=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, default='1', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class User(AbstractUser):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name