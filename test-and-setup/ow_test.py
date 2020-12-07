import requests
import json

with open('../keys.json') as f:
	keys = json.load(f)

url = keys[0]['ow_api']

r = requests.get(url)

print(r.text)