# @snowinginithaca & @snowedinithaca

## About

Two companion Twitter bots, [@snowinginithaca](https://twitter.com/snowinginithaca) & [@snowedinithaca](https://twitter.com/snowedinithaca) report on snow patterns in Ithaca, NY.

Snowing in Ithaca is a small passion project, begun summer 2014, when data was collected by looking out the window. After 2017, tweets were compiled by [IFTTT](https://ifttt.com/) triggers. As of December 2020, current weather data is sourced using the [OpenWeather API](https://openweathermap.org/api) and pushed with [Tweepy](https://www.tweepy.org/).

Snowed in Ithaca was created in 2020 to reply to its companion with the last year it snowed on a given date and index NOAA history for the day's snow record. Snowed in Ithaca currently references a CSV containing NOAA data and tweets with Tweepy. This bot also uses [pytz](https://pypi.org/project/pytz/) and [dateutil](https://dateutil.readthedocs.io/en/stable/) to navigate timezones and dates.

NOAA data is sourced from [Cornell University's weather station](https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USC00304174/detail), with local weather data from 1893-present. Snowed in Ithaca only replies if more than half an inch of snow was recorded. Both bots are hosted on [AWS Lambda](https://aws.amazon.com/).

These bots were built as part of coursework for Pratt School of Information INFO 664, [Programming for Cultural Heritage](http://pfch.nyc/) with Matt Miller in Fall 2020.

## Directory

* ow_twit.py
	* this is the script that runs Snowing in Ithaca
* blizzard_bot.py
	* this is the script that currently runs Snowed in Ithaca
* noaa_reply.py
	* former Snowed in Ithaca script
* test-and-setup
	* this folder contains sections of code that were later combined into the two main scripts

## Requirements

Installing dependencies:

```
pip3 install tweepy
pip3 install pytz
pip3 install python-dateutil
```

API tokens required:
* Twitter API v1 token
* OpenWeather API token