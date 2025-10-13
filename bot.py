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

# Authenticate with Tweepy Client (v2)
try:
    client = tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_SECRET
    )
except Exception as e:
    print(f"Authentication failed: {e}")
    sys.exit(1)

# Load lyrics
with open("lyrics.json", "r") as f:
    lyrics = json.load(f)

# Pick a random lyric
lyric_to_post = random.choice(lyrics)

# Add random emoji to reduce chances of duplicate rejection
emojis = ["🎵", "🎶", "✨", "🎤", "⭐"]
lyric_to_post = f"{lyric_to_post} {random.choice(emojis)}\n#JusticeForZubeenGarg"

# Post tweet
try:
    client.create_tweet(text=lyric_to_post)
    print(f"Posted lyric:\n{lyric_to_post}")
except Exception as e:
    print(f"Failed to post lyric: {e}")
    sys.exit(1)
