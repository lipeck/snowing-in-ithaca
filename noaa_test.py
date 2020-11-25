import requests
import json

with open('keys.json') as f:
	keys = json.load(f)

api_token = keys[0]['noaa_api']

from noaa.noaa_api_v2 import NOAAData

data = NOAAData(api_token)

categories = data.data_categories(locationid='FIPS:37', sortfield='name')

for i in categories:
    print(i)