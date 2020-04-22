from django.contrib import admin

from .models import Artist

# admin.site.register(Artist)

# Define the admin class
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('artist_name', 'prenom', 'surnom', 'phone_number', 'link')

# Register admin class with associated model
admin.site.register(Artist, ArtistAdmin)
