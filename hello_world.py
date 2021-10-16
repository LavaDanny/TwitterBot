import webbrowser 
import tweepy
import consumer_keys

consumer_key = consumer_keys.get_consumer_key()
consumer_secret = consumer_keys.get_consumer_secret()

access_token =  consumer_keys.get_access_token()
access_secret = consumer_keys.get_access_secret()

callback_uri = 'oob'

# authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)

# get user pin and tokens
redirect_url = auth.get_authorization_url()
webbrowser.open(redirect_url)
user_pin_input = input("What is the pin value? ")
auth.get_access_token(user_pin_input)

# create API object
api = tweepy.API(auth)

# get twitter handle
settings = api.get_settings()
print(settings['screen_name'])

# create a tweet
api.update_status("Hello Tweepy")