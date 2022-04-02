# Write a unittest test suite to test the rescrape module

import unittest
import rescrape


class TestRescrape(unittest.TestCase):

    def setUp(self):
        self.url = "https://codingnomads.github.io/recipes/"

    def test_get_page_content(self):
        page = rescrape.get_page_content(self.url)
        self.assertEqual(page.status_code, 200)

    def test_get_html_content(self):
        html = rescrape.get_page_content(self.url).text
        self.assertEqual(rescrape.get_page_content(self.url).text, html)

    # def test_make_soup(self):
    #     pass

    # def test_get_recipe_links(self):
    #     pass

    # def test_get_author(self):
    #     pass

    # def test_get_recipe(self):
    #     pass


if __name__ == "__main__":
    unittest.main() 
