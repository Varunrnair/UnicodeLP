from django.contrib.auth.models import User
from django.db import models


class List(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField(max_length=200 ,default="")
    Complete=models.BooleanField(default=False)
    Userr=models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    def __str__(self):
        return self.title
