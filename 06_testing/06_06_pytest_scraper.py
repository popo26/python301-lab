# Install `pytest` in a virtual environment and rewrite the test suite
# for your web scraper using `pytest` instead of `unittest`.

import pytest
import unittest
import rescrape
from bs4 import BeautifulSoup

"""How to use fixture for setup and teardown: 
https://www.youtube.com/watch?v=JJmTO95AoqE
Not working at the moment;-( """

# @pytest.fixture(scope='module')
# def setup():
url = "https://codingnomads.github.io/recipes/"
html = rescrape.get_page_content(url).text
soup = BeautifulSoup(html, "html.parser")
index_html = rescrape.get_html_content(url)
index_soup = rescrape.make_soup(index_html)
recipe_links = rescrape.get_recipe_links(index_soup)

def test_get_page_content():
    page = rescrape.get_page_content(url)
    assert page.status_code == 200

def test_get_html_content():
    html = rescrape.get_page_content(url).text
    assert rescrape.get_page_content(url).text == html

def test_make_soup():
    assert rescrape.make_soup(html) == soup

def test_get_recipe_links():
    links = [link["href"] for link in soup.find_all("a")]
    assert rescrape.get_recipe_links(soup) == links

def test_get_author():
    for r_link in recipe_links:
        URL = f"{url}/{r_link}"
        soup = rescrape.make_soup(rescrape.get_html_content(URL))
        author = soup.find("p", class_="author").text.strip("by ")
        assert rescrape.get_author(soup), author

def test_get_recipe():
    for r_link in recipe_links:
        URL = f"{url}/{r_link}"
        soup = rescrape.make_soup(rescrape.get_html_content(URL))
        recipe = soup.find("div", class_="md").text
        assert rescrape.get_recipe(soup) == recipe
