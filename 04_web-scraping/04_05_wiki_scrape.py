# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

import requests
from bs4 import BeautifulSoup
import re

URL = "https://en.wikipedia.org/wiki/Web_scraping"
page = requests.get(URL)

soup = BeautifulSoup(page.text, features="html.parser")

links = soup.find_all("a")

all_links= []
for item in links:
   all_links.append(item.get("href"))

links_only = []
for item in all_links:
    #What starswith() statement is doing is, first it is checking if the value is None or not . Then if the value is not None then it is moving forward to make the check using startswith
    if item and item.startswith("http"):
        links_only.append(item)
    #write to a text file
        with open("link_list.txt", "a+") as file:
            file.write(f"\n{item}")

#RegExp

#create a list of only texts in the web page
all_texts = []
for item in links:
    text = item.getText()
    all_texts.append(text)

#convert the list to a string in order to use Regex
list_converted_to_string = " ".join([str(item) for item in all_texts])
print(list_converted_to_string)

#search a number and create a new list
for char in list_converted_to_string:
    num_list = re.findall("[0-9]", list_converted_to_string)
print(num_list)

    



    





