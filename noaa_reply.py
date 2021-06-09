import tweepy
import json
import requests
import datetime
import pytz #for timezones
from noaa.noaa_api_v2 import NOAAData
from dateutil.relativedelta import relativedelta
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
retweet = parsed['retweeted']
reply = parsed['in_reply_to_screen_name']

# check if tweet is retweet or reply, terminate script if so
if retweet == True:
	exit()
if reply != 'null':
	exit()

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
# print(json.dumps(weather_data, indent = 4, sort_keys = True))

#isolate snowfall value & dates
snowfall = weather_data[0]['value']
noaa_date = weather_data[0]['date']

#isolate year for tweet
noaa_year = last_year.strftime('%Y')
noaa_day = last_year.strftime('%B %-d')

#tweet if it snowed on this date last year
if float(snowfall) >= 0.5:
	api.update_status(f"@snowinginithaca the last time it snowed on {noaa_day}, it snowed {str(snowfall)}' in {noaa_year}!", in_reply_to_status_id = tweet_id)
	api.create_favorite(tweet_id)

#set variable for year variable in while loop api call
x = 0

#loops through historical snowfall data to find snowfall on date
while float(snowfall) < 0.5:
		#add 1 to year variable
		x = x+1
		# print(x)
		#create variable to subtract 1 year
		back = last_year - relativedelta(years=int(x))
		#call api but subtract 1 year
		weather_data = data.fetch_data(stationid='GHCND:USC00304174', datasetid='GHCND', startdate=back, enddate=back, datatypeid='SNOW', units='standard')
		#isolate snowfall value & dates from data
		snowfall = weather_data[0]['value']
		noaa_date = weather_data[0]['date']
		#slow down the api!!!
		time.sleep(.5)
		if float(snowfall) >= 0.5:
			#parse date for tweet language
			noaa_year = back.strftime('%Y')
			noaa_day = back.strftime('%B %-d')
			# print()
			#update status
			api.update_status(f"@snowinginithaca the last time it snowed on {noaa_day}, it snowed {str(snowfall)}' in {noaa_year}!", in_reply_to_status_id = tweet_id)
			#fave tweet after reply
			api.create_favorite(tweet_id)
			break