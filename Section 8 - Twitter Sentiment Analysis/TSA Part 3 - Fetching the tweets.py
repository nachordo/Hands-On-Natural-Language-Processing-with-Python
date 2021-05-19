# Twitter Sentiment Analysis using NLP

# Install tweepy - pip install tweepy

# Importing the libraries
import tweepy
import re
import pickle

from tweepy import OAuthHandler

# Please change with your own consumer key, consumer secret, access token and access secret
# Initializing the keys
consumer_key = 'yoIwFkjZGYDa49aO16XqSNqcN'
consumer_secret = 'gl4LQOItV7Z1aFwNrlvaiKJ3t8o8h99blMIAmnmdHxYjzjRAxO' 
access_token = '624310916-E7fDF2IE8P6bfY1oVFglASf6F8RnxMd3vgSXFqnZ'
access_secret ='ID9JcoXHsDcKtvNcnmBGcCQhUlO0wmwAxBJ6LCesiUAas'

# Initializing the tokens
from dotenv import load_dotenv
import os
load_dotenv()
cid=os.getenv("APIKEY") # APISECRET TOKEN
sid=os.getenv("APISECRET") 
tid=os.getenv("TOKEN") 
# Initializing the tokens
auth = tweepy.OAuthHandler(cid, sid)
api = tweepy.API(auth)

# Fetching the tweets
list_tweets = []
args = ['nintendo'];
query = args[0]
if len(args) == 1:
    for status in tweepy.Cursor(api.search,q=query+" -filter:retweets",lang='es',result_type='recent',geocode="40.386741,-3.759804,5000km").items(100):
        list_tweets.append(status.text)
