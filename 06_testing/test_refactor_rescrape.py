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
from bs4 import BeautifulSoup

class TestRefactorRescrape(TestCase):
    
    def setUp(self):
        self.URL = "http://books.toscrape.com/"
        response = requests.get(self.URL)
        data = response.text
        self.soup = BeautifulSoup(data, "html.parser")
        self.price_list_preparation1 = []
        self.price_list_preparation2 = []
        self.price_list_preparation3 = []
    

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
        file = open("result.txt", "a", encoding='utf-8')
        self.assertEqual(file.write("\n-------------Test line----------"), 33)
        file.close()

        """ Delete a line '-------------Test line----------'
            Ref: https://www.geeksforgeeks.org/python-program-to-delete-specific-line-from-file/
        """
        with open("result.txt", "r") as file_read:
            lines = file_read.readlines()
            pointer = 1
            with open("result.txt", "w") as file_write:
                for line in lines:
                    if pointer != 2242:
                        file_write.write(line)
                    pointer += 1  

#can read data from text
    def test_read_data(self):
        file = open("result.txt", "r")
        self.assertIn("<!DOCTYPE html>", file.read())

#can find book title text with CSS selectors
    def test_scrape_price_to_list(self):
        prices = self.soup.select(selector="p", class_="price_color")
        for price in prices:
            p = price.getText().strip("\n, In stock")
            p2 = p.strip('')
            self.price_list_preparation1.append(p2)
        self.assertIn(p2, self.price_list_preparation1)

#can stripping space
    def test_strip_space(self):
        for item in self.price_list_preparation1:
            if item != '':
                self.price_list_preparation2.append(item)
        self.assertNotIn(" ", self.price_list_preparation2)

#can strip Â
    def test_strip_Â(self):
        for item in self.price_list_preparation2:
            final_price = item.split("Â")[1]
            self.price_list_preparation3.append(final_price)
        self.assertNotIn("Â", self.price_list_preparation3)
 

#can find highest book price
    def test_find_highest_price(self):
        self.price_list_preparation3 = refactor_rescrape.find_price()
        self.assertEqual(max(self.price_list_preparation3), "£57.25")
 

#can find the index of the most expensive book
    def test_find_book_title_most_expensive(self):
        self.price_list_preparation3 = refactor_rescrape.find_price()
        highest_price = max(self.price_list_preparation3)
        self.assertEqual(self.price_list_preparation3.index(highest_price), 15)


#can find the title of the most expensive book
    def test_find_title_most_expensive_book(self):
        book_names = refactor_rescrape.find_title()
        self.assertEqual(book_names[15], "Our Band Could Be ...")



if __name__ == "__main__":
    unittest.main()