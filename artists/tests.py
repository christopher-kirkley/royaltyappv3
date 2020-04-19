from django.test import TestCase
from artists.models import Artist

class ArtistPageTest(TestCase):

    def test_renders_artist_template(self):
        response = self.client.get('/artists/')
        self.assertTemplateUsed(response, 'artists/home.html')

    def test_get_artist_list(self):
        response = self.client.get('/artists/all_artists/')
        self.assertEqual(200, response.status_code)
        self.assertNotEqual(response.content.decode(), '')

class ArtistModelTest(TestCase):

    def test_gets_artist_data_from_db(self):
        first_artist = Artist()
        first_artist.artist_name = 'Bob Jones'
        first_artist.prenom = 'Bob'
        first_artist.surnom = 'Jones'
        first_artist.city = 'Timbouctou'
        first_artist.country = 'Mali'
        first_artist.phone_number = '+1122334455'
        first_artist.link = 'http://google.com'
        first_artist.save()

        artists = Artist.objects.all()
        self.assertEqual(len(artists), 1)

        first_saved_artist = artists[0]
        self.assertEqual(first_saved_artist.artist_name, 'Bob Jones')
        self.assertEqual(first_saved_artist.prenom, 'Bob')
        self.assertEqual(first_saved_artist.surnom, 'Jones')
        self.assertEqual(first_saved_artist.city, 'Timbouctou')
        self.assertEqual(first_saved_artist.country, 'Mali')
        self.assertEqual(first_saved_artist.phone_number, '+1122334455')
        self.assertEqual(first_saved_artist.link, 'http://google.com')
    
    def test_passes_artist_data_to_all_artists(self):
        first_artist = Artist()
        first_artist.artist_name = 'Bob Jones'
        first_artist.prenom = 'Bob'
        first_artist.surnom = 'Jones'
        first_artist.city = 'Timbouctou'
        first_artist.country = 'Mali'
        first_artist.phone_number = '+1122334455'
        first_artist.link = 'http://google.com'
        first_artist.save()

        response = self.client.get('/artists/all_artists/')
        returned_json = [
                {'artist_name': 'Bob Jones'},
                {'prenom': 'Bob'},
                {'surnom': 'Jones'},
                {'city': 'Timbouctou'},
                {'country': 'Mali'},
                {'phone_number': '+1122334455'},
                {'link': 'http://google.com'},
                ]
        self.assertIn(returned_json, response.content.decode()) 
        


