import tweepy
import json

with open('../keys.json') as f:
	keys = json.load(f)

consumer_key = keys[0]['twit_api']
consumer_secret = keys[0]['twit_api_secret']
access_token = keys[0]['sw_access']
access_token_secret = keys[0]['sw_access_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#gets @snowinginithaca most recent tweets

status = api.user_timeline(id = 'snowinginithaca', count = 1)[0]

#tweepy parser with help from:
#https://towardsdatascience.com/tweepy-for-beginners-24baf21f2c25

json_str = json.dumps(status._json)
parsed = json.loads(json_str)
data = json.dumps(parsed)

#prints tweet json
# print(json.dumps(parsed, indent = 4, sort_keys = True))

#prints tweet reply id
# print(parsed["id_str"])

tweet_id = parsed['id_str']
fav = parsed['favorited']

#check if tweet has already been replied to, terminate if so
#fav after a reply to mark
if fav == True:
	exit()
else:
	api.update_status('@snowinginithaca tweet', in_reply_to_status_id = tweet_id)
	api.create_favorite(tweet_id)