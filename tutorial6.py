# Tutorial Module 4 - API Interactions - pt.1
# Note: the Google Geocoding exercises require a valid Google API key. This Key was only available during the tutorial
# Get your own? Credentials: https://developers.google.com/maps/documentation/geocoding/get-api-key#get-the-api-key - requires setting up a billed account
 
# Excercise 1

import json
from urllib.request import urlopen
 
baseurl = "https://maps.googleapis.com/maps/api/geocode/json?" # Endpoint URL
query = "address=" + "Australia Zoo" # Build query for address argument
query = query.replace(' ','+') # Replace spaces in query with +
apikey = "&key=AIzaSyCQe15nWsB9Owjl4vo3QzFbD00OD07sIgs" # API key - you will need to get your own to try this example
# I deactivated the API key in this example for safety reasons
 
compiledurl = baseurl + query + apikey # Combining all the url components into a single url
print(compiledurl)
      
# Exercise 2      
 
import json
from urllib.request import urlopen
 
baseurl = "https://maps.googleapis.com/maps/api/geocode/json?" # Endpoint URL
query = "address=" + "Australia Zoo" # Build query for address argument
query = query.replace(' ','+') # Replace spaces in query with +
apikey = "&key=AIzaSyCQe15nWsB9Owjl4vo3QzFbD00OD07sIgs" # API key - you will need to get your own to try this example
# I deactivated the API key in this example for safety reasons
 
compiledurl = baseurl + query + apikey # Combining all the url components into a single url
print(compiledurl)

json_object = urlopen(compiledurl) # Send request + get response
locationdata = json.load(json_object) # Convert JSON result

print(json.dumps(locationdata, sort_keys=True, indent=3))

# Exercise 3

import json
from urllib.request import urlopen
 
baseurl = "https://maps.googleapis.com/maps/api/geocode/json?" # Endpoint URL
query = "address=" + "Australia Zoo" # Build query for address argument
query = query.replace(' ','+') # Replace spaces in query with +
apikey = "&key=AIzaSyCQe15nWsB9Owjl4vo3QzFbD00OD07sIgs" # API key - you will need to get your own to try this example
# I deactivated the API key in this example for safety reasons
 
compiledurl = baseurl + query + apikey # Combining all the url components into a single url
print(compiledurl)

json_object = urlopen(compiledurl) # Send request + get response
locationdata = json.load(json_object) # Convert JSON result

print(json.dumps(locationdata['results'][0]['formatted_address'], sort_keys=True, indent=3))

# Exercise 4

import json
from urllib.request import urlopen
 
baseurl = "https://maps.googleapis.com/maps/api/geocode/json?" # Endpoint URL
query = "address=" + "Australia Zoo" # Build query for address argument
query = query.replace(' ','+') # Replace spaces in query with +
apikey = "&key=AIzaSyCQe15nWsB9Owjl4vo3QzFbD00OD07sIgs" # API key - you will need to get your own to try this example
# I deactivated the API key in this example for safety reasons
 
compiledurl = baseurl + query + apikey # Combining all the url components into a single url
print(compiledurl)

json_object = urlopen(compiledurl) # Send request + get response
locationdata = json.load(json_object) # Convert JSON result

lat = locationdata['results'][0]['geometry']['location']['lat']
lng = locationdata['results'][0]['geometry']['location']['lng']

print(lat,lng)

# Exercise 5

import json
from urllib.request import urlopen
 
baseurl = "https://maps.googleapis.com/maps/api/geocode/json?" # Endpoint URL
query = "address=" + "Australia Zoo" # Build query for address argument
query = query.replace(' ','+') # Replace spaces in query with +
apikey = "&key=AIzaSyCQe15nWsB9Owjl4vo3QzFbD00OD07sIgs" # API key - you will need to get your own to try this example
# I deactivated the API key in this example for safety reasons
 
compiledurl = baseurl + query + apikey # Combining all the url components into a single url
print(compiledurl)

json_object = urlopen(compiledurl) # Send request + get response
locationdata = json.load(json_object) # Convert JSON result

types = locationdata['results'][0]['types']

for type in types:
	print(type)

# Exercise 6

import json
import requests
 
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQABslKgWgXkd-vtojPePATyNiVRVpVvBy7tspjCsdUH0BcqQn-3O17b4ejyTQSev-WuLXwHGveANZn12tfZWLGaKzAqTTHwDI3ItLmqobta8E6Au_5PDnyXuEqAkeFIR6WzotN1J3hGU_CTqWk-Mrmqju5elNf77DM_En2s7AgCP0jvMj2K-7Ez2oYUd6FXc-7YwwzKjzLlAX76eRsreCqgMn3H5mtU9BQ9cZ_S3p143KvKaNF5GlA5CztSURVlNS9ZN_ZBvIYckVqb7Q',
} # You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/?q=tania%20bowra&type=artist&market=&limit=&offset= (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)
 
params = (
        ('q', 'The Beatles'),
        ('type', 'artist'),
    )
 
response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # request the response
# The endpoint base url is supplemented by the arguments in the variables headers and params
print(response) # Optional, informs on whether call was successful (Code [200])
 
json_data = json.loads(response.text) # convert json response to text/dict
 
print(json.dumps(json_data, sort_keys=True, indent=3)) # A beautified print of the returndata
 
###
