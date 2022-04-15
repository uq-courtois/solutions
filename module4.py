import json

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


### Exercise 1: Print all the information for the second shape
print(data['items'][1])

### Exercise 2: Print the first shape’s length and width
print(data['items'][0]['length'])
print(data['items'][0]['width'])

### Exercise 3: For loop through the items and print the shape information
for i in data['items']:
	print(i['shape'])

### NOTE: Google Geocoding API key is a paying key and was only active for the live tutorial.
### Exercise 4: Print the URL you would use for the request in the console and click it (variable compiledurl in the example)
 
import json
from urllib.request import urlopen
 
# Endpoint URL
endpoint = "https://maps.googleapis.com/maps/api/geocode/json?" 
 
# Build query for address argument
query =  'Australia Zoo'
# Replace spaces in query with +
query = query.replace(' ','+') 
 
# API key - you will need to get your own to try this example
# The API key in this example is deactivated for security reasons
apikey = "AIzaSyCCTB2FTaReARpzcgBLLDcwGbjHyLWef-8" 
 
# Combine all the url components into a single url + print url
compiledurl = endpoint + 'address=' + query + '&key=' + apikey 
print(compiledurl)

### NOTE: Google Geocoding API key is a paying key and was only active for the live tutorial.
### Exercise 5: Do the request and print the response in the console (variable data in the example)
 
import json
from urllib.request import urlopen
 
# Endpoint URL
endpoint = "https://maps.googleapis.com/maps/api/geocode/json?" 
 
# Build query for address argument
query =  'Australia Zoo'
# Replace spaces in query with +
query = query.replace(' ','+') 
 
# API key - you will need to get your own to try this example
# The API key in this example is deactivated for security reasons
apikey = "AIzaSyCCTB2FTaReARpzcgBLLDcwGbjHyLWef-8" 
 
# Combine all the url components into a single url + print url
compiledurl = endpoint + 'address=' + query + '&key=' + apikey 
print(compiledurl)
 
# Send request + get response
response = urlopen(compiledurl) 
 
# Convert JSON result -> our data are in the variable data
data = json.load(response) 
 
# Print data variable with hierarchical formatting
print(json.dumps(data, sort_keys=True, indent=3)) 

### NOTE: Google Geocoding API key is a paying key and was only active for the live tutorial.
# Exercise 6: Isolate the formatted address (from data) and print it to the console
 
import json
from urllib.request import urlopen
 
# Endpoint URL
endpoint = "https://maps.googleapis.com/maps/api/geocode/json?" 
 
# Build query for address argument
query =  'Australia Zoo'
# Replace spaces in query with +
query = query.replace(' ','+') 
 
# API key - you will need to get your own to try this example
# The API key in this example is deactivated for security reasons
apikey = "AIzaSyCCTB2FTaReARpzcgBLLDcwGbjHyLWef-8" 
 
# Combine all the url components into a single url + print url
compiledurl = endpoint + 'address=' + query + '&key=' + apikey 
print(compiledurl)
 
# Send request + get response
response = urlopen(compiledurl) 
 
# Convert JSON result -> our data are in the variable data
data = json.load(response) 

# Print formatted address
print(data['results'][0]['formatted_address'])

### NOTE: Google Geocoding API key is a paying key and was only active for the live tutorial.
### Exercise 7: Isolate the longitude and latitude (from data) and print them in the console

import json
from urllib.request import urlopen
 
# Endpoint URL
endpoint = "https://maps.googleapis.com/maps/api/geocode/json?" 
 
# Build query for address argument
query =  'Australia Zoo'
# Replace spaces in query with +
query = query.replace(' ','+') 
 
# API key - you will need to get your own to try this example
# The API key in this example is deactivated for security reasons
apikey = "AIzaSyCCTB2FTaReARpzcgBLLDcwGbjHyLWef-8" 
 
# Combine all the url components into a single url + print url
compiledurl = endpoint + 'address=' + query + '&key=' + apikey 
print(compiledurl)
 
# Send request + get response
response = urlopen(compiledurl) 
 
# Convert JSON result -> our data are in the variable data
data = json.load(response) 

# Print lattitude and longitude
print(data['results'][0]['geometry']['location']['lat'])
print(data['results'][0]['geometry']['location']['lng'])

### NOTE: Google Geocoding API key is a paying key and was only active for the live tutorial.
### Exercise 8: Isolate the types of location (at the bottom of the response, in the variable data) ) and print them in the console


import json
from urllib.request import urlopen
 
# Endpoint URL
endpoint = "https://maps.googleapis.com/maps/api/geocode/json?" 
 
# Build query for address argument
query =  'Australia Zoo'
# Replace spaces in query with +
query = query.replace(' ','+') 
 
# API key - you will need to get your own to try this example
# The API key in this example is deactivated for security reasons
apikey = "AIzaSyCCTB2FTaReARpzcgBLLDcwGbjHyLWef-8" 
 
# Combine all the url components into a single url + print url
compiledurl = endpoint + 'address=' + query + '&key=' + apikey 
print(compiledurl)
 
# Send request + get response
response = urlopen(compiledurl) 
 
# Convert JSON result -> our data are in the variable data
data = json.load(response) 

# Print lattitude and longitude
for i in data['results'][0]['types']:
	print(i)

###############################################################
### ADDITIONAL - SPOTIFY TEST

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
