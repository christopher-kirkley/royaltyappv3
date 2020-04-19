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

if __name__ == "__main__":
    unittest.main()

