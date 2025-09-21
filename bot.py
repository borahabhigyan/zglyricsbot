import tweepy
import json
import os
import random
import sys

API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

with open("lyrics.json", "r") as f:
    lyrics = json.load(f)


last_file = "last_lyric.txt"
last_lyric = None
if os.path.exists(last_file):
    with open(last_file, "r") as f:
        last_lyric = f.read().strip()


lyric_to_post = random.choice(lyrics)
while lyric_to_post == last_lyric and len(lyrics) > 1:
    lyric_to_post = random.choice(lyrics)


try:
    client.create_tweet(text=lyric_to_post)
    print(f"Posted lyric: {lyric_to_post}")

   
    with open(last_file, "w") as f:
        f.write(lyric_to_post)
