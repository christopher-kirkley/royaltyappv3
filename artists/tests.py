from django.test import TestCase

class ArtistPageTest(TestCase):

    def test_renders_artist_template(self):
        response = self.client.get('/artists/')
        self.assertTemplateUsed(response, 'artists/home.html')
