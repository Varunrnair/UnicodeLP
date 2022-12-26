from django.db import models
from users.models import *
from django.conf import settings

class Competition(models.Model):
    com_name       = models.CharField(max_length= 200, primary_key=True)
    com_winner     = models.CharField(max_length=200, default="no winners")
    
    def __str__(self):
        return self.com_name

class Footballclub(models.Model):
    fc_id          = models.IntegerField(primary_key=True)
    club_logo      = models.CharField(max_length=240)
    fc_name        = models.CharField(max_length=255)
    description    = models.TextField(default="") 
    fc_email       = models.EmailField() 
    fc_stadium     = models.TextField(default="")  
    fc_location    = models.TextField(default="")  
    competing      = models.ForeignKey(Competition, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.fc_name

class Match(models.Model):
    match_timing   = models.TextField(default="")
    match_location = models.TextField(primary_key=True)  
    playedby       = models.ForeignKey(Footballclub, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.match_locatio

class Player(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    jersey = models.IntegerField(default="")

    def __str__(self):
        return self.user