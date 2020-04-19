from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from artists.models import Artist

def home_page(request):
    return render(request, 'artists/home.html')

def all_artists(request):
    all_artists = serializers.serialize("json", Artist.objects.all())
    return HttpResponse(all_artists)

