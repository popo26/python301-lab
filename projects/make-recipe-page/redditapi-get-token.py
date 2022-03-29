# Demonstrate how you can log in to the Reddit API to receive content that
# requires authentication, using only `requests` and your credentials.


import requests
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv('client_secret')
password = os.getenv('password')
user_agent = os.getenv('user_agent')
username = os.getenv('username')
access_token= os.getenv('access_token')



"""Ref: 
https://alpscode.com/blog/how-to-use-reddit-api/
https://github.com/reddit-archive/reddit/wiki/OAuth2 
"""


'''Get access token - Expires in an hour'''
# base_url = "https://www.reddit.com/"
# data = {'grant_type': 'password', 'username': username, 'password': password}
# auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
# r = requests.post(base_url + 'api/v1/access_token',
#                   data=data,
#                   headers={'user-agent': f'{client_id} by {username}'},
#                   auth=auth
# )

# d = r.json()
# print(d)


token = 'bearer ' + access_token

base_url = 'https://oauth.reddit.com'

search_topics = {'q': 'Curry', 'limit': 25, 'sort': "hot"} 
headers = {'Authorization': token, 'User-Agent': f'{client_id} by {username}'}
response = requests.get(base_url + '/r/Curry/search', headers=headers, params=search_topics)

print(response.status_code)
data = response.text

with open("curry_info_with_only_redditapi.txt", "w") as file:
    file.write(data)

#Below is to check all the titles in json file.
# data2 = response.json()
# title_list = []
# x = data2["data"]["children"]

# for i in range(len(x)):
#     y = x[i]["data"]["title"]
#     title_list.append(y)
# print(title_list)



