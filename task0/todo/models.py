from calendar import c
from django.db import models


class List(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField(max_length=200 ,default="")
    Complete=models.BooleanField(default=False)
    def __str__(self):
        return self.title
