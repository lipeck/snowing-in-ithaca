import requests
import json
import tweepy

with open('keys.json') as f:
	keys = json.load(f)

url = keys[0]['ow_api']
consumer_key = keys[0]['twit_api']
consumer_secret = keys[0]['twit_api_secret']
access_token = keys[0]['sw_access']
access_token_secret = keys[0]['sw_access_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#get weather data
r = requests.get(url)
data = r.json()

#isolate weather data
weather = data['weather']

#isolate current condition
for current in weather:
    condition = current['main']

#tweet if snowing
if condition == 'Snow':
	api.update_status('yes')
elif condition == 'Clear':
	api.update_status('no')

# print(condition)