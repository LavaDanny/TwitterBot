import webbrowser 
import tweepy
import consumer_keys
import os
import json

consumer_key = consumer_keys.get_consumer_key()
consumer_secret = consumer_keys.get_consumer_secret()

access_token =  consumer_keys.get_access_token()
access_secret = consumer_keys.get_access_secret()

callback_uri = 'oob'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
auth.set_access_token(access_token, access_secret)

# get user pin and tokens
redirect_url = auth.get_authorization_url()
webbrowser.open(redirect_url)
user_pin_input = input("What is the pin value? ")
auth.get_access_token(user_pin_input)

# Create API object
api = tweepy.API(auth)

# get tweets mentioning "aliens"
tweets = api.search_tweets("aliens")

for i in tweets:
    print(i.text)