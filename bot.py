import tweepy
import os
import json
import random

# Load keys
BEARER_TOKEN = os.environ["BEARER_TOKEN"]
API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]

# Use Tweepy v2 client
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

# Load lyrics
with open("lyrics.json", "r") as f:
    lyrics = json.load(f)

lyric_to_post = random.choice(lyrics)

# Post tweet using v2 endpoint
try:
    response = client.create_tweet(text=lyric_to_post)
    print(f"Posted lyric: {lyric_to_post}")
except Exception as e:
    print(f"Failed to post lyric: {e}")

