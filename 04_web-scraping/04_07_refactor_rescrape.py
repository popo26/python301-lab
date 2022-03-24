# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.

import requests
from bs4 import BeautifulSoup

# URL = "http://books.toscrape.com/"

# response = requests.get(URL)
# data = response.text

# soup = BeautifulSoup(data, "html.parser")

# #Find book title text with CSS selectors
# items = soup.select(selector="h3", name="a")

# book_names = []
# for item in items:
#     book_name = item.getText()
#     book_names.append(book_name)

# #Find book price with CSS selectors
# prices = soup.select(selector="p", class_="price_color")

# price_list_preparation1 = []
# for price in prices:
#     p = price.getText().strip("\n, In stock")
#     p2 = p.strip('')
#     price_list_preparation1.append(p2)

# #Stripping space " ". 
# price_list_preparation2 = []
# for item in price_list_preparation1:
#     if item != '':
#         price_list_preparation2.append(item)

# #stripping Â.
# price_list_preparation3 = []
# for item in price_list_preparation2:
#     final_price = item.split("Â")[1]
#     price_list_preparation3.append(final_price)

# highest_price = max(price_list_preparation3)
# index = price_list_preparation3.index("£57.25")

# print(f"Most expensive book in this page is \"{book_names[15]}\" and {price_list_preparation2[15]}.")



###WITH FUNCTIONS

# URL = "http://books.toscrape.com/"
# response = requests.get(URL)
# data = response.text

# file = open("result.txt", "w")
# file.write(data)

file = open("result.txt", "r")
data = file.read()

soup = BeautifulSoup(data, "html.parser")

#Find book title text with CSS selectors
def find_title():
    items = soup.select(selector="h3", name="a")
    book_names = []
    for item in items:
        book_name = item.getText()
        book_names.append(book_name)
    return book_names
    

#Find book price with CSS selectors
def find_price():
    #Stripping space " " .
    prices = soup.select(selector="p", class_="price_color")
    price_list_preparation1 = []
    for price in prices:
        p = price.getText().strip("\n, In stock")
        p2 = p.strip('')
        price_list_preparation1.append(p2)
    #Stripping and Â. 
    price_list_preparation2 = []
    for item in price_list_preparation1:
        if item != '':
            price_list_preparation2.append(item)
    #Final price list.
    price_list_preparation3 = []
    for item in price_list_preparation2:
        final_price = item.split("Â")[1]
        price_list_preparation3.append(final_price)
    return price_list_preparation3
 
  
book_names = find_title()
price_list_preparation3 = find_price()

highest_price = max(price_list_preparation3)
index = price_list_preparation3.index("£57.25")

print(f"Most expensive book in this page is \"{book_names[15]}\" and {price_list_preparation3[15]}.")

file.close()


