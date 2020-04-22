from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.views import generic


from artists.models import Artist

def home(request):
    artists = Artist.objects.all()
    return render(request, 'artists/home.html', {'artists': artists})

def all_artists(request):
    all_artists = serializers.serialize("json", Artist.objects.all())
    return HttpResponse(all_artists)

def add(request):
    if request.method == 'POST':
        artist_name = request.POST['artist_name']
        prenom = request.POST['prenom']
        surnom = request.POST['surnom']
        Artist.objects.create(
                artist_name=artist_name,
                prenom=prenom,
                surnom=surnom,
                ) 
        return redirect('/artists/')

    return render(request, 'artists/add.html')

def edit(request, pk):
    artist = Artist.objects.get(pk=pk)
    if request.method == 'POST':
        artist.prenom = request.POST['prenom']
        artist.save()
        return redirect('/artists/')

    return render(request, 'artists/detail.html', {'artist': artist})
