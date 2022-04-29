### EXERCISE 1 - Use the Spotify Search Endpoint to print all returned artist information for BTS

import json
import requests
 
# You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/ (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)
token = 'BQDxdpvuuhlnQsQARr8My4LyqN0GiD3_nMUdX7Z3MfSYe1dwyFAnnzrjX1_C8kW8Fr3svTONsG1jwmp9XVQKyID7CtoEylLI55oT31is_YIzpWquAS0T4dl'
 
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token,
} 
 
# Set parameters
params = (
        ('q', 'Taylor Swift'),
        ('type', 'artist'),
				('limit', '1'),
    )
 
# Make request
response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # 
 
# We want code [200] here, points to a successful request
print(response) 
 
# Convert response to text/dict
data = json.loads(response.text) 

# Print all data
print(json.dumps(data, sort_keys=True, indent=3))

### EXERCISE 2 - Use the Spotify Search Endpoint to get artist information for BTS and print the band’s popularity score

import json
import requests
 
# You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/ (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)
token = 'BQDxdpvuuhlnQsQARr8My4LyqN0GiD3_nMUdX7Z3MfSYe1dwyFAnnzrjX1_C8kW8Fr3svTONsG1jwmp9XVQKyID7CtoEylLI55oT31is_YIzpWquAS0T4dl'
 
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token,
} 
 
# Set parameters
params = (
        ('q', 'Taylor Swift'),
        ('type', 'artist'),
				('limit', '1'),
    )
 
# Make request
response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # 
 
# We want code [200] here, points to a successful request
print(response) 
 
# Convert response to text/dict
data = json.loads(response.text)

# Print popularity
popularity = data['artists']['items'][0]['popularity']
print(popularity)

### EXERCISE 3 - Use the Spotify Search Endpoint to get artist information for BTS and print the band’s genres

import json
import requests
 
# You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/ (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)
token = 'BQDxdpvuuhlnQsQARr8My4LyqN0GiD3_nMUdX7Z3MfSYe1dwyFAnnzrjX1_C8kW8Fr3svTONsG1jwmp9XVQKyID7CtoEylLI55oT31is_YIzpWquAS0T4dl'
 
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token,
} 
 
# Set parameters
params = (
        ('q', 'Taylor Swift'),
        ('type', 'artist'),
				('limit', '1'),
    )
 
# Make request
response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # 
 
# We want code [200] here, points to a successful request
print(response) 
 
# Convert response to text/dict
data = json.loads(response.text)

# Print popularity
genres = data['artists']['items'][0]['genres']
print(genres)

### Exercise 4
# Use the Spotify Search Endpoint to get artist information for all artists in https://digitalanalytics.id.au/static/files/sp-artists.csv 
# Read the file, loop though its entries and use the key ['artist']to do repeated API queries
# Print the genres of all the artists

import pandas as pd
import json
import requests

data = pd.read_csv('https://digitalanalytics.id.au/static/files/sp-artists.csv',sep=',')
data = data.T.to_dict().values()

for i in data:
	print(i['artist'])

	token = 'BQDxdpvuuhlnQsQARr8My4LyqN0GiD3_nMUdX7Z3MfSYe1dwyFAnnzrjX1_C8kW8Fr3svTONsG1jwmp9XVQKyID7CtoEylLI55oT31is_YIzpWquAS0T4dl'
	 
	headers = {
	    'Accept': 'application/json',
	    'Content-Type': 'application/json',
	    'Authorization': 'Bearer ' + token,
	} 
	 
	# Set parameters
	params = (
	        ('q', i['artist']),
	        ('type', 'artist'),
					('limit', '1'),
	    )
	 
	# Make request
	response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # 
	 
	# We want code [200] here, points to a successful request
	print(response) 
	 
	# Convert response to text/dict
	data = json.loads(response.text)
	
	# Print popularity
	genres = data['artists']['items'][0]['genres']
	print(genres)

### Exercise 5
# Use the Spotify Search Endpoint to get track information for In Your Eyes by The Weeknd
# Use the query string: 'in your eyes the weeknd' + print the track’s id

import json
import requests
 
# You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/ (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)
token = 'BQDxdpvuuhlnQsQARr8My4LyqN0GiD3_nMUdX7Z3MfSYe1dwyFAnnzrjX1_C8kW8Fr3svTONsG1jwmp9XVQKyID7CtoEylLI55oT31is_YIzpWquAS0T4dl'
 
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token,
} 
 
# Set parameters
params = (
        ('q', 'Taylor Swift Shake it off'),
        ('type', 'track'),
				('limit', '1'),
    )
 
# Make request
response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # 
 
# We want code [200] here, points to a successful request
print(response) 
 
# Convert response to text/dict
data = json.loads(response.text) 
 
# Isolating the track id
trackid = data['tracks']['items'][0]['id']
print(trackid)

### Excercise 6
# Use the Spotify Audio Features endpoint to get audio features for In Your Eyes by The Weeknd
# Use the track’s id obtained in the previous exercise (7szuecWAPwGoV1e5vGu8tl)
# Print all information

import json
import requests

# You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/ (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)

token = 'BQDxdpvuuhlnQsQARr8My4LyqN0GiD3_nMUdX7Z3MfSYe1dwyFAnnzrjX1_C8kW8Fr3svTONsG1jwmp9XVQKyID7CtoEylLI55oT31is_YIzpWquAS0T4dl'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token,
} 
 
# Add in the trackid, here we use the one for Taylor Swift's Shake it off
trackid = "7szuecWAPwGoV1e5vGu8tl"

# Make request
response = requests.get('https://api.spotify.com/v1/audio-features/'+trackid, headers=headers)

# We want code [200] here, points to a successful request
print(response) 

# Convert response to text/dict
data = json.loads(response.text) 

# Print raw result
print(json.dumps(data, sort_keys=True, indent=3)) 

### Excercise 7
# Use the Spotify Audio Features endpoint to get audio features for In Your Eyes by The Weeknd
# Use the track’s id obtained in the previous exercise (7szuecWAPwGoV1e5vGu8tl)
# Print the value of tempo

import json
import requests

# You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/ (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)

token = 'BQDxdpvuuhlnQsQARr8My4LyqN0GiD3_nMUdX7Z3MfSYe1dwyFAnnzrjX1_C8kW8Fr3svTONsG1jwmp9XVQKyID7CtoEylLI55oT31is_YIzpWquAS0T4dl'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token,
} 
 
# Add in the trackid, here we use the one for Taylor Swift's Shake it off
trackid = "7szuecWAPwGoV1e5vGu8tl"

# Make request
response = requests.get('https://api.spotify.com/v1/audio-features/'+trackid, headers=headers)

# We want code [200] here, points to a successful request
print(response) 

# Convert response to text/dict
data = json.loads(response.text) 

# Print tempo
print(data['tempo'])
