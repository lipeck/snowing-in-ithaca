# slightly modified from:
# https://stackoverflow.com/questions/41065856/is-it-possible-to-add-multiple-accounts-to-a-twitter-app-twitter-api-bot

import tweepy
import json

with open('keys.json') as f:
	keys = json.load(f)

consumer_token = keys[0]['twit_api']
consumer_secret = keys[0]['twit_api_secret']

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print("Error! Failed to get access token.")

print(redirect_url)

verifier = input('Verifier:')

try:
    auth.get_access_token(verifier)
except tweepy.TweepError:
    print("Error! PIN is wrong. Failed to get access token.")

new_token = auth.access_token
new_secret = auth.access_token_secret

print("access_token: " + new_token)
print("access_token_secret: " + new_secret)