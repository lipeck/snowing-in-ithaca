import tweepy #pip
import json
import requests #pip (incl in tweepy)
import datetime
import pytz #pip #for timezones
from noaa.noaa_api_v2 import NOAAData #local folder
from dateutil.relativedelta import relativedelta #pip
import time

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

#pulling out data from tweet
tweet_id = parsed['id_str']
fav = parsed['favorited']
tweet_date = parsed['created_at']

# check if tweet has already been replied to, terminate script if so
if fav == True:
	exit()

#reformats tweet date to ISO & changes timezone from UTC to eastern
date_iso = datetime.datetime.strptime(tweet_date, '%a %b %d %H:%M:%S %z %Y')
date_iso_est = date_iso.astimezone(pytz.timezone('America/New_York'))

#isolate date for NOAA
date_clean = date_iso_est.strftime('%Y-%m-%d')

#subtract one year from tweet date
noaa_date = datetime.datetime.strptime(date_clean, '%Y-%m-%d').date()
last_year = noaa_date - relativedelta(years=1)

#return snowfall data for last year
data = NOAAData(api_token)
weather_data = data.fetch_data(stationid='GHCND:USC00304174', datasetid='GHCND', startdate=last_year, enddate=last_year, datatypeid='SNOW', units='standard')

#print snowfall data for last year
print(json.dumps(weather_data, indent = 4, sort_keys = True))

#isolate snowfall value & dates
snowfall = weather_data[0]['value']
noaa_date = weather_data[0]['date']

#isolate year for tweet
noaa_year = last_year.strftime('%Y')
noaa_day = last_year.strftime('%B %-d')

if float(snowfall) >= 0.5:
	# print('on this date it last snowed ' + str(snowfall) + '" in ' + noaa_year)
	api.update_status('@snowinginithaca the last time it snowed on ' + noaa_day + ', it snowed ' + str(snowfall) + '" in ' + noaa_year + '!', in_reply_to_status_id = tweet_id)
	api.create_favorite(tweet_id)

#set variable for while loop
x = 0

#fave tweet after a reply to mark
while float(snowfall) < 0.5:
		x = x+1
		print(x)
		back = last_year - relativedelta(years=int(x))
		weather_data = data.fetch_data(stationid='GHCND:USC00304174', datasetid='GHCND', startdate=back, enddate=back, datatypeid='SNOW', units='standard')
		snowfall = weather_data[0]['value']
		noaa_date = weather_data[0]['date']
		time.sleep(1)
		if float(snowfall) >= 0.5:
			noaa_year = back.strftime('%Y')
			noaa_day = back.strftime('%B %-d')
			# print()
			api.update_status('@snowinginithaca the last time it snowed on ' + noaa_day + ', it snowed ' + str(snowfall) + '" in ' + noaa_year + '!', in_reply_to_status_id = tweet_id)
			api.create_favorite(tweet_id)
			break