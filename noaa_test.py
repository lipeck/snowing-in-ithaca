import requests
import json

with open('keys.json') as f:
	keys = json.load(f)

api_token = keys[0]['noaa_api']

from noaa.noaa_api_v2 import NOAAData
data = NOAAData(api_token)

test_date = '2013-12-20'

#returns weather data
weather_data = data.fetch_data(stationid='GHCND:USC00304174', datasetid='GHCND', startdate='2013-12-10', enddate=test_date, datatypeid='SNOW', units='standard')

#prints snowing station data
print(json.dumps(weather_data, indent = 4, sort_keys = True))