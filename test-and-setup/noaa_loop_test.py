import requests
import json
import datetime
from dateutil.relativedelta import relativedelta
import time

with open('keys.json') as f:
	keys = json.load(f)

api_token = keys[0]['noaa_api']

from noaa.noaa_api_v2 import NOAAData
data = NOAAData(api_token)

date_clean = '2020-01-24'

#subtracts one year from date
noaa_date = datetime.datetime.strptime(date_clean, '%Y-%m-%d').date()
last_year = noaa_date - relativedelta(years=1)

#returns snowfall data for date
weather_data = data.fetch_data(stationid='GHCND:USC00304174', datasetid='GHCND', startdate=last_year, enddate=last_year, datatypeid='SNOW', units='standard')

#prints snowfall data for date
# print(json.dumps(weather_data, indent = 4, sort_keys = True))

#isolate snowfall value & date
snowfall = weather_data[0]['value']
noaa_date = weather_data[0]['date']

#sets variable for while loop
x = 0

while float(snowfall) == 0:
		x = x+1
		# print(x)
		back = last_year - relativedelta(years=int(x))
		weather_data = data.fetch_data(stationid='GHCND:USC00304174', datasetid='GHCND', startdate=back, enddate=back, datatypeid='SNOW', units='standard')
		snowfall = weather_data[0]['value']
		noaa_date = weather_data[0]['date']
		time.sleep(1)
		if float(snowfall) > 0:
			print('it snowed ' + str(snowfall) + ' ' + noaa_date)
			break