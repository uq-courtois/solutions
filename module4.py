### Exercise 1

import json
# Needed for exercises 1-3 -> copy/paste until row of hashes

data = {
   "items": [
		 {
			 'shape':'rectangle',
			 'length':4,
			 'width':5
		 },
		 {
			 'shape':'square',
			 'length':4,
			 'width':4
		 },
		 {
			 'shape':'cube',
			 'length':4,
			 'width':4,
			 'height':4
		 },
   ]
}
print(json.dumps(data, sort_keys=True, indent=3)) 

###############################################################
### ADDITIONAL

import requests
import json

token = 'PASTE YOUR TOKEN HERE'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+token,
}

params = {
	'time_range': 'medium_term',
	'limit':'50'
}

response = requests.get('https://api.spotify.com/v1/me/top/artists', headers=headers, params=params)
print(response)
data = json.loads(response.text) 

for i in data['items']:
	print(i['name']+';')
	
# https://docs.google.com/forms/d/1o4ZaSYEY1MRM64d42Z_N7V8QphNnbIvf35u2dODA4-k/viewform
