# Revisit one of the previous lab exercises that were challenging for you.
# Write a test suite that checks for the correct functionality of the code.
# Then try to refactor your solution, maybe you can make the code more
# concise or more elegant? Keep checking whether you broke the functionality
# by repeatedly running your test suite against your changes.


from unittest import TestCase
import unittest
import requests
import refactor_rescrape
from pathlib import Path

class TestRefactorRescrape(TestCase):
    
    def setUp(self):
        self.URL = "http://books.toscrape.com/"

#can connect to API successfully
    def test_api_connection(self):
        response = requests.get(self.URL)
        self.assertEqual(response.status_code, 200)

#can get text data from the API
    def test_get_text_from_api(self):
        response = requests.get(self.URL)
        self.assertIn('<!DOCTYPE html>', response.text)

#check if result.txt exists
    def test_file_exists(self):
        path = Path("result.txt")
        self.assertEqual(path.is_file(), True)

#can write data to result.txt
    def test_write_data(self):
        file = open("result.txt", "a")
        self.assertEqual(file.write("\n-------------Test line----------"), 33)
        #Add a line to delete "-------------Test line----------"
        file.close()

#can read data from text
    def test_read_data(self):
        file = open("result.txt", "r")
        self.assertIn("-------------Test line----------", file.read())

#can find book title text with CSS selectors

#can find book price with CSS selectors

 





if __name__ == "__main__":
    unittest.main()