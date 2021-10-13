import webbrowser 
import tweepy

consumer_key = "34bepI0KblEkA2S8yPOyxylZu"
consumer_secret = "DYsOFKrjrP8TLOYZ0ure05yczaFseF9p3eVSc3hrTuMzTM6nGC"

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