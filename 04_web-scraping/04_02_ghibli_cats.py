# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi.herokuapp.com/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.


import requests


BASE_URL = "https://ghibliapi.herokuapp.com/species/603428ba-8a86-4b0b-a9f1-65df6abef3d3"

response = requests.get(BASE_URL)
data = response.json()

cat_links = data["people"]

cat_ids = []
for link in cat_links:
    cat_ids.append(link.split("/")[4])
print(cat_ids)

cat_list = []
for cat_id in cat_ids:
    cat = []
    CAT_URL = f"https://ghibliapi.herokuapp.com/people/{cat_id}"
    response = requests.get(CAT_URL)
    data = response.json()
    cat.append(data["name"])
    cat.append(data["gender"])
    cat.append(data["eye_color"])
    cat.append(data["hair_color"])
    cat_list.append(cat)
print(cat_list)







