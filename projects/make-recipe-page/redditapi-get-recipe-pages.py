# Using the external `praw` package, fetch recipes through the Reddit API
# and re-build the CodingNomads recipe collection website.
# If you commit this code to GitHub, make sure to keep your API secrets
# out of version control, for example by adding them as environment variables.

import praw
import requests
from dotenv import load_dotenv
import os
import webbrowser

load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv('client_secret')
password = os.getenv('password')
user_agent = os.getenv('user_agent')
username = os.getenv('username')
access_token= os.getenv('access_token')


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


reddit = praw.Reddit(
    client_id = os.getenv("client_id"),
    client_secret = os.getenv('client_secret'),
    password = os.getenv('password'),
    user_agent = os.getenv('user_agent'),
    username = os.getenv('username'),
    access_token= os.getenv('access_token'), #Get the token by enabling line 25 to 35 once expired.
)

#Ref: https://praw.readthedocs.io/en/stable/code_overview/models/subreddit.html
subreddit = reddit.subreddit("Curry")

submission_titles = []
submission_urls = []
submission_upvote_ratios = []
for submission in reddit.subreddit("Curry").hot(limit=25):
    submission_titles.append(submission.title) 
    submission_urls.append(submission.url)
    submission_upvote_ratios.append(submission.upvote_ratio)

#Reorder 3 lists based on upvote descending order.
submission_upvote_ratios, submission_titles, submission_urls = zip(*sorted(zip(submission_upvote_ratios, submission_titles, submission_urls ), reverse=True))

html_file = ""
html_file += "<div><body style='text-align:center;background-color:black'><img src='https://media.giphy.com/media/fsiJbn1CeRVsXB22cE/giphy.gif'><h1 style='color:#C69B7B;font-size;bold;'>Feel like curry?</h1></body></div><div><body style='background-color:red'>"
for i in range(len(submission_titles)):
    html_file += '<a style="color:white;font-family:verdana;font-size:22px;font-size:bold;" href="{}">{}</a>'.format(submission_urls[i], submission_titles[i])
    html_file += '<p style="color:red">upvote:{}</p><br>'.format(submission_upvote_ratios[i])
html_file += "</body></div>"

with open("curry.html", "w") as file:
    file.write(html_file)

webbrowser.open("curry.html")





    


