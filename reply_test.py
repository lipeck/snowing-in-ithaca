import tweepy
import json

with open('keys.json') as f:
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

# print(json.dumps(parsed, indent = 4, sort_keys = True))

#tweet reply id
print(parsed["id_str"])

# reply to tweet
# api.update_status('@snowinginithaca tweet', in_reply_to_status_id = '1332819373002813446')
