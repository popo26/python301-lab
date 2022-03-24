# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

##Scrape book titles and prices on this first page and find the most expensive book.##
import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/"

response = requests.get(URL)
data = response.text

soup = BeautifulSoup(data, "html.parser")

#Find book title text with CSS selectors
items = soup.select(selector="h3", name="a")

book_names = []
for item in items:
    book_name = item.getText()
    book_names.append(book_name)

#Find book price with CSS selectors
prices = soup.select(selector="p", class_="price_color")

price_list_preparation1 = []
for price in prices:
    p = price.getText().strip("\n, In stock")
    p2 = p.strip('')
    price_list_preparation1.append(p2)

#Stripping space " ". 
price_list_preparation2 = []
for item in price_list_preparation1:
    if item != '':
        price_list_preparation2.append(item)

#stripping Â.
price_list_preparation3 = []
for item in price_list_preparation2:
    final_price = item.split("Â")[1]
    price_list_preparation3.append(final_price)

highest_price = max(price_list_preparation3)
index = price_list_preparation3.index("£57.25")

print(f"Most expensive book in this page is \"{book_names[15]}\" and {price_list_preparation3[15]}.")
    
