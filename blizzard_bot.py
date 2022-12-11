import tweepy
import json
import requests
import datetime
import pytz #for timezones
from noaa.noaa_api_v2 import NOAAData
from dateutil.relativedelta import relativedelta
import time
import csv

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
if reply != None:
	exit()

# check if tweet has already been replied to, terminate script if so
if fav == True:
	exit()

#reformats tweet date to ISO & changes timezone from UTC to eastern
date_iso = datetime.datetime.strptime(tweet_date, '%a %b %d %H:%M:%S %z %Y')
date_iso_est = date_iso.astimezone(pytz.timezone('America/New_York'))

#isolate date for NOAA
date_clean = date_iso_est.strftime('%Y-%m-%d')
date_csv = date_iso_est.strftime('-%m-%d')

# setting variables for loops
last = lastsnow = maxsnowfall = 0
big_blizzard = ''

# reads weather data on csv
with open('snowfall.csv', 'r') as f:
	reader = csv.DictReader(f)
	
	for row in reader:

		# check dates & convert snowfall values to integers
		date_col = row['DATE']
		snow = float(row['SNOW'])

		# checks for blizzard
		if date_csv in date_col:
			if snow > maxsnowfall:
				maxsnowfall = snow
				big_blizzard = date_col

		else: continue
	
		# checks for last snow
		if date_csv in date_col and snow >= 0.5:
			
			if last < int(date_col[:4]):
				last = int(date_col[:4])
				lastsnow = snow

		else: continue

# round whole numbers
if lastsnow.is_integer() == True:
	lastsnow = int(lastsnow)

if maxsnowfall.is_integer() == True:
	print(maxsnowfall)
	maxsnowfall = int(maxsnowfall)

if last == 0: exit()
			
if last == int(big_blizzard[:4]):

	# isolate year for tweet & separate out date info
	blizzard = datetime.datetime.strptime(big_blizzard,'%Y-%m-%d')
	blizzard_year = blizzard.strftime('%Y')
	blizzard_day = blizzard.strftime('%B %-d')

	# tweet & fav
	api.update_status(f'@snowinginithaca the last time it snowed in Ithaca on {blizzard_day}, it snowed {lastsnow}" in {blizzard_year}! that\'s the most recorded snowfall!', in_reply_to_status_id = tweet_id)
	api.create_favorite(tweet_id)

	print(f'@snowinginithaca the last time it snowed in Ithaca on {blizzard_day}, it snowed {lastsnow}" in {blizzard_year}! that\'s the most recorded snowfall!')

if last != int(big_blizzard[:4]) and lastsnow > 0 and maxsnowfall > 0:

	# isolate year for tweet & separate out date info
	blizzard = datetime.datetime.strptime(big_blizzard,'%Y-%m-%d')
	blizzard_year = blizzard.strftime('%Y')
	blizzard_day = blizzard.strftime('%B %-d')

	# tweet & fav
	api.update_status(f'@snowinginithaca the last time it snowed in Ithaca on {blizzard_day}, it snowed {lastsnow}\" in {last}. the most snow recorded on this day is {maxsnowfall}\" in {blizzard_year}!', in_reply_to_status_id = tweet_id)
	api.create_favorite(tweet_id)

	# print(f'@snowinginithaca the last time it snowed in Ithaca on {blizzard_day}, it snowed {lastsnow}\" in {last}. the most snow recorded on this day is {maxsnowfall}\" in {blizzard_year}!')
