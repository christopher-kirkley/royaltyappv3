import unittest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

class BrowserTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path = '/Users/ck/python/geckodriver/geckodriver')
        self.browser.get('http://localhost:8000/artists/')
    
    def tearDown(self):
        self.browser.quit()

    def test_artist_page_loads(self):
        title = self.browser.title
        self.assertEqual(title, 'Artists')

    # Looking at page, lists all the current artists in a table
    def test_artist_table_is_populated(self):
        rows = self.browser.find_elements_by_id('tr')
        self.assertNotEqual(len(rows), 0)

    # On the right there is an edit button to change the artist details

    # When clicking the edit button, the fields are fillable

    # Clicking out the table is update with the new artist info

if __name__ == "__main__":
    unittest.main()

