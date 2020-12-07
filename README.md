# @snowinginithaca & @snowedinithaca

## About

Two companion Twitter bots, [@snowinginithaca](https://twitter.com/snowinginithaca) & [@snowedinithaca](https://twitter.com/snowedinithaca) both analyze weather patterns in Ithaca, NY. 

Snowing in Ithaca is a small passion project, started in 2014, when I collected data by looking out the window. After 2017, tweets were compiled by [IFTTT](https://ifttt.com/) triggers. Now, in 2020, current weather data is sourced using the [OpenWeather API](https://openweathermap.org/api) and pushed with [Tweepy](https://www.tweepy.org/).

Snowed in Ithaca is a new bot that replies to its companion with the last year it snowed on a given date. Snowed in Ithaca calls on the [NOAA Web Services v2 API](https://www.ncdc.noaa.gov/cdo-web/webservices/v2#gettingStarted) alongside @crvaden's [NOAA API module](https://github.com/crvaden/NOAA_API_v2) and also tweets with Tweepy. This bot also uses [pytz](https://pypi.org/project/pytz/) and [dateutil](https://dateutil.readthedocs.io/en/stable/) to navigate timezones and dates.

NOAA data is sourced from [Cornell University's weather station](https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USC00304174/detail), with local weather data from 1893-present. Snowed in Ithaca only replies if more than half an inch of snow was recorded. Both bots are hosted on [AWS Lambda](https://aws.amazon.com/).

These bots were built as part of coursework for Pratt School of Information [INFO 664](http://pfch.nyc/).

## Directory

* ow_twit.py
	* this is the script that runs Snowing in Ithaca
* noaa_reply.py
	* this is the script that runs Snowed in Ithaca
* test-and-setup
	* this folder contains sections of code that were later combined into the two main scripts

## Requirements

Installing dependencies:

```
pip3 install tweepy
pip3 install pytz
pip3 install python-dateutil
git submodule add https://github.com/crvaden/NOAA_API_v2 noaa
```

API tokens required:
* Twitter API v1 token
* NOAA Web Services v2 API token
* OpenWeather API token