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

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQAutymB1gVCft1ra_LiMAYq-rXsTVsGfFBs0QbneWcGSCEru_ajkM6NbOvuDY1ocQg3N8cpmu1mguCuT5pmebkAv0-gnl00H5UTfohbbReSSRM0uPHTmyhjXjGBTBmrsi8rXabITrGTfdP0pWxJ8C-p1cWp8eVaHQuGmHz9jjl_St8TtjlQT2_7a6Hvz-rQqst8UHze8UhRN8ryjuIN42Z5znqRuVmzxJhDn0UiJxl5ZydiMZUONJwrCbZqP9rXCPA7I6PGopG5V8ON5PVUtDI',
}

params = {
    'time_range': 'medium_term',
		'limit':'50'
}

response = requests.get('https://api.spotify.com/v1/me/top/artists', headers=headers, params=params)
data = json.loads(response.text) 

for i in data['items']:
	print(i['name']+';')
	
# https://docs.google.com/forms/d/1o4ZaSYEY1MRM64d42Z_N7V8QphNnbIvf35u2dODA4-k/viewform?edit_requested=true&fbzx=4792520770300365509
