import tweepy #pip
import json
import requests #pip (incl in tweepy)
# from datetime import date #for todays date
import datetime
import pytz #pip #for timezones
from noaa.noaa_api_v2 import NOAAData

with open('keys.json') as f:
	keys = json.load(f)

consumer_key = keys[0]['twit_api']
consumer_secret = keys[0]['twit_api_secret']
access_token = keys[0]['sw_access']
access_token_secret = keys[0]['sw_access_secret']
api_token = keys[0]['noaa_api']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#gets @snowinginithaca most recent tweet

status = api.user_timeline(id = 'snowinginithaca', count = 1)[0]

#tweepy parser with help from: https://towardsdatascience.com/tweepy-for-beginners-24baf21f2c25

json_str = json.dumps(status._json)
parsed = json.loads(json_str)
data = json.dumps(parsed)

#prints tweet in readable format
# print(json.dumps(parsed, indent = 4, sort_keys = True))

tweet_id = parsed['id_str']
fav = parsed['favorited']
tweet_date = parsed['created_at']

# check if tweet has already been replied to, terminate script if so
if fav == True:
	exit()

#reformats tweet date to ISO & changes timezone from UTC to eastern
date_iso = datetime.datetime.strptime(tweet_date, '%a %b %d %H:%M:%S %z %Y')
date_iso_est = date_iso.astimezone(pytz.timezone('America/New_York'))

#isolate date
date_clean = date_iso_est.strftime('%Y-%m-%d')

print(date_clean)

data = NOAAData(api_token)

#returns snowfall data for date of last tweet
weather_data = data.fetch_data(stationid='GHCND:USC00304174', datasetid='GHCND', startdate=date_clean, enddate=date_clean, datatypeid='SNOW', units='standard')

#prints data
print(json.dumps(weather_data, indent = 4, sort_keys = True))

# #fave tweet after a reply to mark
# 	api.update_status('@snowinginithaca tweet', in_reply_to_status_id = tweet_id)
# 	api.create_favorite(tweet_id)


