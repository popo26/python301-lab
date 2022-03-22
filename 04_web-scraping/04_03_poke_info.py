# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5


import requests
import json
from pprint import pprint

# BASE_URL = "https://pokeapi.co/api/v2/berry"

# response = requests.get(BASE_URL)
# data = response.json()

# with open("pokemon.json", "w") as file:
#     json.dump(data, file)
# print(data)

# with open("pokemon.json", "r") as file:
#     data = json.load(file)

# cheri = data["results"][0]["name"]
# chesto = data["results"][1]["name"]
# pecha = data["results"][2]["name"]
# rawst = data["results"][3]["name"]
# aspear = data["results"][4]["name"]
# leppa = data["results"][5]["name"]

names = ["cheri", "chesto", "pecha", "rawst", "aspear", "leppa"]

pokemon_charactors = []
for name in names:
    item = []
    BASE_URL = f"https://pokeapi.co/api/v2/berry/{name}"
    response = requests.get(BASE_URL)
    data = response.json()
    # print(data)
    item.append(data["id"])
    item.append(data["name"])
    item.append(data["natural_gift_type"])
    # print(item)
    pokemon_charactors.append(item)
print(pokemon_charactors)











