# Twitter Sentiment Analysis using NLP

# Install tweepy - pip install tweepy

# Importing the libraries
import tweepy
import re
import pickle

import tweepy 

#Please change with your own consumer key, consumer secret, access token and access secret
# Initializing the keys
consumer_key = 'yoIwFkjZGYDa49aO16XqSNqcN'
consumer_secret = 'gl4LQOItV7Z1aFwNrlvaiKJ3t8o8h99blMIAmnmdHxYjzjRAxO' 
access_token = '624310916-E7fDF2IE8P6bfY1oVFglASf6F8RnxMd3vgSXFqnZ'
access_secret ='ID9JcoXHsDcKtvNcnmBGcCQhUlO0wmwAxBJ6LCesiUAas'

from dotenv import load_dotenv
import os
load_dotenv()
cid=os.getenv("APIKEY") # APISECRET TOKEN
sid=os.getenv("APISECRET") 
tid=os.getenv("TOKEN") 
# Initializing the tokens
auth = tweepy.AppAuthHandler(cid, sid)
api = tweepy.API(auth)
#auth.set_access_token(access_token, access_secret)
#args = ['trump'];
#api = tweepy.API(auth,timeout=10)
