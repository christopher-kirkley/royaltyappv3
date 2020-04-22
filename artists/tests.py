from django.test import TestCase
from artists.models import Artist


class ArtistModelTest(TestCase):

    def setUp(self):
        first_artist = Artist.objects.create(
                artist_name = 'Bob Jones',
                prenom = 'Bob',
                surnom = 'Jones',
                city = 'Timbouctou',
                country = 'Mali',
                phone_number = '+1122334455',
                link = 'http://google.com',
                )

        second_artist = Artist.objects.create(
                artist_name = 'Smo Rock',
                prenom = 'Smo',
                surnom = 'Rock',
                city = 'Salvador',
                country = 'Brazil',
                phone_number = '+22299',
                link = 'http://yahoo.com',
                )

    def test_gets_artist_data_from_db(self):
        artists = Artist.objects.all()
        self.assertEqual(len(artists), 2)

        first_saved_artist = artists[0]
        self.assertEqual(first_saved_artist.artist_name, 'Bob Jones')
        self.assertEqual(first_saved_artist.prenom, 'Bob')
        self.assertEqual(first_saved_artist.surnom, 'Jones')
        self.assertEqual(first_saved_artist.city, 'Timbouctou')
        self.assertEqual(first_saved_artist.country, 'Mali')
        self.assertEqual(first_saved_artist.phone_number, '+1122334455')
        self.assertEqual(first_saved_artist.link, 'http://google.com')
    
        second_saved_artist = artists[1]
        self.assertEqual(second_saved_artist.artist_name, 'Smo Rock')
        self.assertEqual(second_saved_artist.prenom, 'Smo')
        self.assertEqual(second_saved_artist.surnom, 'Rock')
        self.assertEqual(second_saved_artist.city, 'Salvador')
        self.assertEqual(second_saved_artist.country, 'Brazil')
        self.assertEqual(second_saved_artist.phone_number, '+22299')
        self.assertEqual(second_saved_artist.link, 'http://yahoo.com')
    
    def test_artist_page_returns_artists(self):
        response = self.client.get('/artists/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.context['artists'].count(), 2)
        
    def test_artist_detail_page(self):
        response = self.client.get('/artists/1/')
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'artists/detail.html')
        # self.assertIn('Bob Jones', response.content.decode())
        # self.assertIn('Timbouctou', response.content.decode())
        # self.assertIn('Mali', response.content.decode())
        # self.assertIn('+1122334455', response.content.decode())
        # self.assertIn('http://google.com', response.content.decode())
        

class AddArtistTest(TestCase):

    def test_uses_template(self):
        response = self.client.get('/artists/add_artist/')
        self.assertEqual(response.status_code, 200)

    def test_add_artist_to_database(self):
        data = {
                'artist_name': 'Bob Jones',
                'prenom': 'Bob',
                'surnom': 'Jones',
                }
        response = self.client.post('/artists/add_artist/', data=data)
        artists = Artist.objects.all()
        self.assertEqual(len(artists), 1)
        self.assertEqual(response.status_code, 302)
        

class ArtistHomePageTest(TestCase):

    def test_uses_template(self):
        response = self.client.post('/artists/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'artists/home.html')


class ArtistUpdateDetailsTest(TestCase):

    def setUp(self):
        first_artist = Artist.objects.create(
                artist_name = 'Bob Jones',
                prenom = 'Bob',
                surnom = 'Jones',
                city = 'Timbouctou',
                country = 'Mali',
                phone_number = '+1122334455',
                link = 'http://google.com',
                )

    def test_updates_artist(self):
        response = self.client.post('/artists/1/', data={'prenom':'Job'})
        self.assertEqual(response.status_code, 302)
        artists = Artist.objects.all()
        first_artist = artists[0]
        self.assertEqual(first_artist.prenom, 'Job')
  

