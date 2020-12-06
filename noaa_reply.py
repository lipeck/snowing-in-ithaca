import tweepy #pip
import json
import requests #pip (incl in tweepy)
# from datetime import date #for todays date
import datetime
import pytz #pip #for timezones

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

#tweepy parser with help from:
#https://towardsdatascience.com/tweepy-for-beginners-24baf21f2c25

json_str = json.dumps(status._json)
parsed = json.loads(json_str)
data = json.dumps(parsed)

#prints tweet in readable format
# print(json.dumps(parsed, indent = 4, sort_keys = True))

#prints tweet reply id
# print(parsed["id_str"])

# tweet_id = parsed['id_str']
# fav = parsed['favorited']

tweet_date = parsed['created_at']

#reformats tweet date
date_iso = datetime.datetime.strptime(tweet_date, '%a %b %d %H:%M:%S %z %Y')

#isolates year etc
# print(date_iso.strftime('%Y'))

date_iso_est = date_iso.astimezone(pytz.timezone('America/New_York'))

print(date_iso_est)


print('tweet date - ' + str(tweet_date))
print('date iso - ' + str(date_iso_est))

#check if tweet has already been replied to, terminate if so
#fav after a reply to mark

# if fav == True:
# 	exit()
# else:
# 	api.update_status('@snowinginithaca tweet', in_reply_to_status_id = tweet_id)
# 	api.create_favorite(tweet_id)


# from noaa.noaa_api_v2 import NOAAData
# data = NOAAData(api_token)

# test_date = '2013-12-20'

# #returns weather data
# weather_data = data.fetch_data(stationid='GHCND:USC00304174', datasetid='GHCND', startdate=test_date, enddate=test_date, datatypeid='SNOW', units='standard')

# #prints snowing station data
# print(json.dumps(weather_data, indent = 4, sort_keys = True))