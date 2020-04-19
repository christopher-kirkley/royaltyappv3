from django.db import models

class Artist(models.Model):
    artist_name = models.TextField(default='')
    prenom = models.TextField(default='')
    surnom = models.TextField(default='')
    city = models.TextField(default='')
    country = models.TextField(default='')
    phone_number = models.TextField(default='')
    link = models.TextField(default='')

