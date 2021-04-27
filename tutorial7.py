### API pt 2
### Response [401]: Do not forget to replace the API token with an active one...

### Exercise 1

import json
import requests
 
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQAw-sNUDTh3nvbM604iBCz_UvabwGUaVGk9Pzzr8iCikYkdo4CFgGJr93WIMyNanK80o3egMWoHazIvux5Sn7K5HYvQdhIOR6LtmwDFvhNKslnjasHGCOkNlVnf1cy03WaMEKYK5LJWVD2B_ZVOWfRcat0d5YZkUUUzAPP4_if3Zr4Ek4vaGbKLa4hRRFkbaU_lZst-qJWKKKW151u6n26ElvyEaqI4PNfR6fH-fCSB32jIwFgr2nWHbEkGzwRlrkGLQZkj1R_j14JeyXr20m4',
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
 
### Exercise 2

import json
import requests
from urllib.request import Request, urlopen

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQAw-sNUDTh3nvbM604iBCz_UvabwGUaVGk9Pzzr8iCikYkdo4CFgGJr93WIMyNanK80o3egMWoHazIvux5Sn7K5HYvQdhIOR6LtmwDFvhNKslnjasHGCOkNlVnf1cy03WaMEKYK5LJWVD2B_ZVOWfRcat0d5YZkUUUzAPP4_if3Zr4Ek4vaGbKLa4hRRFkbaU_lZst-qJWKKKW151u6n26ElvyEaqI4PNfR6fH-fCSB32jIwFgr2nWHbEkGzwRlrkGLQZkj1R_j14JeyXr20m4',
} # You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/?q=tania%20bowra&type=artist&market=&limit=&offset= (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)
 
params = (
        ('q', 'The Beatles'),
        ('type', 'artist'),
    )
 
response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # request the response
# The endpoint base url is supplemented by the arguments in the variables headers and params
print(response) # Optional, informs on whether call was successful (Code [200])
 
json_data = json.loads(response.text) # convert json response to text/dict
 
imgurl = json_data['artists']['items'][0]['images'][0]['url'] # Isolate img url

imgfile = open('beatles.jpg','wb') # Create a new, empty picture file
imgfile.write(urlopen(imgurl).read()) # Write picture information into empty file
imgfile.close() # Close file
 
print('Picture downloaded...')

### Exercise 3

import json
import requests
from urllib.request import Request, urlopen

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQAw-sNUDTh3nvbM604iBCz_UvabwGUaVGk9Pzzr8iCikYkdo4CFgGJr93WIMyNanK80o3egMWoHazIvux5Sn7K5HYvQdhIOR6LtmwDFvhNKslnjasHGCOkNlVnf1cy03WaMEKYK5LJWVD2B_ZVOWfRcat0d5YZkUUUzAPP4_if3Zr4Ek4vaGbKLa4hRRFkbaU_lZst-qJWKKKW151u6n26ElvyEaqI4PNfR6fH-fCSB32jIwFgr2nWHbEkGzwRlrkGLQZkj1R_j14JeyXr20m4',
} # You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/?q=tania%20bowra&type=artist&market=&limit=&offset= (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)
 
params = (
        ('q', 'The Beatles'),
        ('type', 'artist'),
    )
 
response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # request the response
# The endpoint base url is supplemented by the arguments in the variables headers and params
print(response) # Optional, informs on whether call was successful (Code [200])
 
json_data = json.loads(response.text) # convert json response to text/dict
 
print(json_data['artists']['items'][0]['id']) # Print artist ID 

### Exercise 4

import json
import requests
from urllib.request import Request, urlopen

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQAw-sNUDTh3nvbM604iBCz_UvabwGUaVGk9Pzzr8iCikYkdo4CFgGJr93WIMyNanK80o3egMWoHazIvux5Sn7K5HYvQdhIOR6LtmwDFvhNKslnjasHGCOkNlVnf1cy03WaMEKYK5LJWVD2B_ZVOWfRcat0d5YZkUUUzAPP4_if3Zr4Ek4vaGbKLa4hRRFkbaU_lZst-qJWKKKW151u6n26ElvyEaqI4PNfR6fH-fCSB32jIwFgr2nWHbEkGzwRlrkGLQZkj1R_j14JeyXr20m4',
} # You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/?q=tania%20bowra&type=artist&market=&limit=&offset= (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)
 
params = (
        ('q', 'lucy in the sky with diamonds'),
        ('type', 'track'),
				('limit', '1')
    )
 
response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # request the response
# The endpoint base url is supplemented by the arguments in the variables headers and params
print(response) # Optional, informs on whether call was successful (Code [200])
 
json_data = json.loads(response.text) # convert json response to text/dict
 
print(json.dumps(json_data['tracks']['items'][0]['album']['name'], sort_keys=True, indent=3)) # Print first 

### Exercise 5

import json
import requests
from urllib.request import Request, urlopen

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQAw-sNUDTh3nvbM604iBCz_UvabwGUaVGk9Pzzr8iCikYkdo4CFgGJr93WIMyNanK80o3egMWoHazIvux5Sn7K5HYvQdhIOR6LtmwDFvhNKslnjasHGCOkNlVnf1cy03WaMEKYK5LJWVD2B_ZVOWfRcat0d5YZkUUUzAPP4_if3Zr4Ek4vaGbKLa4hRRFkbaU_lZst-qJWKKKW151u6n26ElvyEaqI4PNfR6fH-fCSB32jIwFgr2nWHbEkGzwRlrkGLQZkj1R_j14JeyXr20m4',
} # You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/?q=tania%20bowra&type=artist&market=&limit=&offset= (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)
 
params = (
        ('q', 'lucy in the sky with diamonds'),
        ('type', 'track'),
				('limit', '1')
    )
 
response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # request the response
# The endpoint base url is supplemented by the arguments in the variables headers and params
print(response) # Optional, informs on whether call was successful (Code [200])
 
json_data = json.loads(response.text) # convert json response to text/dict
 
print(json.dumps(json_data['tracks']['items'][0]['id'], sort_keys=True, indent=3)) # Print track id

### Exercise 6

import requests
import json
 
# Setting headers 
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQAw-sNUDTh3nvbM604iBCz_UvabwGUaVGk9Pzzr8iCikYkdo4CFgGJr93WIMyNanK80o3egMWoHazIvux5Sn7K5HYvQdhIOR6LtmwDFvhNKslnjasHGCOkNlVnf1cy03WaMEKYK5LJWVD2B_ZVOWfRcat0d5YZkUUUzAPP4_if3Zr4Ek4vaGbKLa4hRRFkbaU_lZst-qJWKKKW151u6n26ElvyEaqI4PNfR6fH-fCSB32jIwFgr2nWHbEkGzwRlrkGLQZkj1R_j14JeyXr20m4',
}
# You need to change the Authorization code each into your own fresh API Token, e.g., at the bottom of this page:
# https://developer.spotify.com/console/get-recommendations/

artistid = '3WrFJ7ztbogyGnTHbHJFl2'
trackid = '25yQPHgC35WNnnOUqFhgVR'

# Setting parameters
params = (
    ('seed_artists', artistid),
    ('seed_tracks', trackid),
)
 
response = requests.get('https://api.spotify.com/v1/recommendations', headers=headers, params=params) # Making request
print(response) # Optional, informs on whether call was successful (Code [200])
json_data = json.loads(response.text) # Converting response into Python data structure
 
# Printing the tracks by artists, one by one
for track in json_data['tracks']:
	print(track['name'],'by',track['album']['artists'][0]['name'])
  
### Exercise 7

import requests
import json

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQAw-sNUDTh3nvbM604iBCz_UvabwGUaVGk9Pzzr8iCikYkdo4CFgGJr93WIMyNanK80o3egMWoHazIvux5Sn7K5HYvQdhIOR6LtmwDFvhNKslnjasHGCOkNlVnf1cy03WaMEKYK5LJWVD2B_ZVOWfRcat0d5YZkUUUzAPP4_if3Zr4Ek4vaGbKLa4hRRFkbaU_lZst-qJWKKKW151u6n26ElvyEaqI4PNfR6fH-fCSB32jIwFgr2nWHbEkGzwRlrkGLQZkj1R_j14JeyXr20m4',
}

response = requests.get('https://api.spotify.com/v1/audio-features/25yQPHgC35WNnnOUqFhgVR', headers=headers)

json_data = json.loads(response.text) # convert json response to text/dict

print(json.dumps(json_data['tempo'], sort_keys=True, indent=3)) # A beautified print of the returndata

### Exercise 8

import requests
import json

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQAw-sNUDTh3nvbM604iBCz_UvabwGUaVGk9Pzzr8iCikYkdo4CFgGJr93WIMyNanK80o3egMWoHazIvux5Sn7K5HYvQdhIOR6LtmwDFvhNKslnjasHGCOkNlVnf1cy03WaMEKYK5LJWVD2B_ZVOWfRcat0d5YZkUUUzAPP4_if3Zr4Ek4vaGbKLa4hRRFkbaU_lZst-qJWKKKW151u6n26ElvyEaqI4PNfR6fH-fCSB32jIwFgr2nWHbEkGzwRlrkGLQZkj1R_j14JeyXr20m4',
}

trackid = '25yQPHgC35WNnnOUqFhgVR'

response = requests.get('https://api.spotify.com/v1/audio-features/'+trackid, headers=headers)

json_data = json.loads(response.text) # convert json response to text/dict

print(json.dumps(json_data['acousticness'], sort_keys=True, indent=3)) # A beautified print of the returndata
 
### Exercise 9

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import json
 
url = 'https://www.imdb.com/title/tt0386676/' 
 
headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = Request(url, headers=headers)
context = ssl._create_unverified_context()

uClient= urlopen(req, context=context)
html = uClient.read()
uClient.close()
soup = BeautifulSoup(html, 'html.parser')

jsonobject = soup.find('script',type='application/ld+json').string
imdbdata = json.loads(jsonobject)

actors = imdbdata['actor']

for actor in actors:
	print(actor['name'])
  
### Exercise 10

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import json
 
url = 'https://www.imdb.com/title/tt0386676/' 
 
headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = Request(url, headers=headers)
context = ssl._create_unverified_context()

uClient= urlopen(req, context=context)
html = uClient.read()
uClient.close()
soup = BeautifulSoup(html, 'html.parser')

jsonobject = soup.find('script',type='application/ld+json').string
imdbdata = json.loads(jsonobject)

print(imdbdata['description'])
