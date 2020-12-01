import requests
import json

with open('keys.json') as f:
	keys = json.load(f)

api_token = keys[0]['noaa_api']

from noaa.noaa_api_v2 import NOAAData

data = NOAAData(api_token)

weather_data = data.fetch_data(datasetid='GHCND', locationid='ZIP:14850', startdate='2020-01-01', enddate='2020-01-02')

# for i in categories:
#     print(i)

print(json.dumps(weather_data, indent = 4, sort_keys = True))