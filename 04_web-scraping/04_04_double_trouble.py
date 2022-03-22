# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.

import requests
import random

GHIBULI_URL = "https://ghibliapi.herokuapp.com/people?limit=6"

response = requests.get(GHIBULI_URL)
data = response.json()

ghibli_charactors = []
for i in range(0, len(data)):
    item = []
    # item.append(data[i]["id"])
    item.append(data[i]["name"])
    item.append(data[i]["species"])
    # print(item)
    ghibli_charactors.append(item)
print(ghibli_charactors)


