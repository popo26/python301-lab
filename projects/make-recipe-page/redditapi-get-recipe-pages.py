# Using the external `praw` package, fetch recipes through the Reddit API
# and re-build the CodingNomads recipe collection website.
# If you commit this code to GitHub, make sure to keep your API secrets
# out of version control, for example by adding them as environment variables.

import praw
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Read here for Authentication etc : https://github.com/reddit-archive/reddit/wiki/OAuth2

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
PASSWORD = os.getenv('PASSWORD')
USERAGENT = os.getenv('USERAGENT')
USERNAME = os.getenv('USERNAME')


reddit = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    password="PASSWORD",
    user_agent="USERAGENT",
    username="USERNAME",
)

