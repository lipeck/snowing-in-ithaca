import requests
import json
import datetime
from dateutil.relativedelta import relativedelta

with open('keys.json') as f:
	keys = json.load(f)

api_token = keys[0]['noaa_api']

from noaa.noaa_api_v2 import NOAAData
data = NOAAData(api_token)

test_date = '2013-12-20'


#subtracts one year from date
date_clean = datetime.datetime.strptime(test_date, '%Y-%m-%d').date()
last_year = date_clean - relativedelta(years=1)

# print(last_year)

#returns weather data
weather_data = data.fetch_data(stationid='GHCND:USC00304174', datasetid='GHCND', startdate=last_year, enddate=last_year, datatypeid='SNOW', units='standard')

# #prints snowing station data
# # print(json.dumps(weather_data, indent = 4, sort_keys = True))

#isolates snowfall data
snowfall = weather_data[0]['value']

print(snowfall)