from django.db import models

class Artist(models.Model):
    artist_name = models.CharField(max_length=200, unique=True, null=False)
    prenom = models.CharField(max_length=50, null=False)
    surnom = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=20, blank=True, default='')
    country = models.CharField(max_length=20, blank=True, default='')
    phone_number = models.CharField(max_length=30, blank=True, default='')
    link = models.CharField(max_length=200, blank=True, default='') 
    
    def __str__(self):
        return self.artist_name

