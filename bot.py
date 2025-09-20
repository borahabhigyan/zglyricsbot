import tweepy
import json
import os
import random
import sys

# Load Twitter API keys from environment variables
API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]

# Authenticate with Tweepy
try:
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
except Exception as e:
    print(f"Authentication failed: {e}")
    sys.exit(1)

# Load lyrics
with open("lyrics.json", "r") as f:
    lyrics = json.load(f)

# Choose a random lyric to tweet
lyric_to_post = random.choice(lyrics)

# Post tweet
try:
    api.update_status(lyric_to_post)
    print(f"Posted lyric: {lyric_to_post}")
except Exception as e:
    print(f"Failed to post lyric: {e}")
    sys.exit(1)