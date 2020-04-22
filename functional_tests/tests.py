from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

class BrowserTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path = '/Users/ck/python/geckodriver/geckodriver')
        self.browser.get(self.live_server_url + '/artists/')
    
    def tearDown(self):
        self.browser.quit()

    def test_artist_page_loads(self):
        title = self.browser.title
        self.assertEqual(title, 'Artists')

        """Displays a list of artists."""
        artist_list = self.browser.find_element_by_id('artist-list')
        self.assertIn('Artist List', artist_list.text) 
        
        """User goes to add a new artist."""
        add_artist_button = self.browser.find_element_by_id('add-artist')
        add_artist_button.click()

        """Button takes user to add artist page."""
        self.assertIn('Add Artist', self.browser.title) 
        
        """User fills out form for new artist and clicks submit."""
        input_artist_name = self.browser.find_element_by_id('artist_name')
        input_prenom = self.browser.find_element_by_id('prenom')
        input_surnom = self.browser.find_element_by_id('surnom')
        input_artist_name.send_keys('Bob Jones')
        input_prenom.send_keys('Bob')
        input_surnom.send_keys('Jones')
        self.browser.find_element_by_id('artist-submit').submit()

        """User automatically returns to main artist page."""
        time.sleep(1)
        title = self.browser.title
        self.assertEqual(title, 'Artists')
        
        """Artist that was added is now on artist page."""
        artist_list = self.browser.find_element_by_id('artist-list')
        self.assertIn('Bob Jones', artist_list.text)
        
        """User clicks on artist to view artist page."""
        artist_link = self.browser.find_element_by_id('artist-link')
        artist_link.click()

        """Artist Page loads."""
        time.sleep(1)
        title = self.browser.title
        self.assertEqual(title, 'Artist')

        """User decides to edit the name of the artist. User changes
        artist prenom and submits the update."""
        input_prenom = self.browser.find_element_by_id('prenom')
        input_prenom.send_keys('Job')
        self.browser.find_element_by_id('artist-update').submit()
        time.sleep(1)

        """User automatically returns to artist page."""
        title = self.browser.title
        self.assertEqual(title, 'Artists')
        
        """User checks that artist name was updated"""
        artist_link = self.browser.find_element_by_id('artist-link')
        artist_link.click()
        artist_prenom = self.browser.find_element_by_id('artist-prenom')
        self.assertIn('Job', artist_prenom.text)

        

        

if __name__ == "__main__":
    unittest.main()

