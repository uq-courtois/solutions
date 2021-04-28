### Exercise 1 - Module 1a

#Define a list 'x' with the following integer values: 9,8,7,3,5
x = [9,8,7,3,5]

#Append the integer value 2
x.append(2)

#Print the first element of the list to the console
print(x[0])

#Define a list of dictionaries that contains the info from the following table:

#Name	Income
#Lisa	3400
#Sam	2120
#Jasmine	1240

data = [
	{'Name':'Lisa','Income':3400},
	{'Name':'Sam','Income':2120},
	{'Name':'Jasmine','Income':1240},
]

#Change Sam's income to 2240

data[1]['income'] = 2240

#Isolate and print Sam's updated income from the list of dicts

print(data[1]['income'])

### Exercise 2 - Module 1b

# Define a variable named ‘dataset’ that contains the following information:

# Artist	Track	Plays
# Dire Straits	Sultans of Swing	65
# Pink Floyd	Comfortably Numb	23
# The Smiths	Cemetery Gates	15
# Nick Cave & The Bad Seeds	The Ship Song	36
# Dire Straits	Brothers in Arms	20

dataset = [
	{'Artist':'Dire Straits','Track':'Sultans of Swin','Plays':65},
	{'Artist':'Pink Floyd','Track':'Comfortably Numb','Plays':23},
	{'Artist':'The Smiths','Track':'Cemetery Gates','Plays':15},
	{'Artist':'Nick Cave & The Bad Seeds','Track':'The Ship Song','Plays':36},
	{'Artist':'Dire Straits','Track':'Brothers in Arms','Plays':20},
]

#Print the artist and track (title) of songs with more than 20 plays. Each artist and track combination is printed on a separate line.

for d in dataset:
	if d['Plays'] > 20:
		print(d['Artist'],'-',d['Track'])

#Print all track titles of songs by Dire Straits and Pink Floyd. Printing just the titles is ok, each title is printed on a separate line.

for d in dataset:
	if d['Artist'] == 'Dire Straits' or d['Artist'] == 'Pink Floyd':
		print(d['Track'])

#Print the total number of plays. This is the total number of plays of all 5 songs.

plays = []

for d in dataset:
	plays.append(d['Plays'])

print(sum(plays))

### Exercise 3 - Module 2

#Read in the file artistsong.csv (Available at http://digitalanalytics.id.au/static/files/artistsong.csv).

import pandas as pd

data = pd.read_csv('http://digitalanalytics.id.au/static/files/artistsong.csv',sep=';')
data = data.T.to_dict().values()
 
#Write the information of songs with 20 or more plays into a new file called artistsong_filtered.csv (i.e., artist, track, plays).

datatowrite = []

for item in data:
	if item['Plays'] >= 20:
		datatowrite.append(item)

data = pd.DataFrame(datatowrite)
data.to_csv('artistsong_filtered.csv',sep=';',index=False)

# Exercise 4 - Module 3

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.abc.net.au/news/justin'

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}
req = Request(url, headers=headers)
context = ssl._create_unverified_context()

uClient = urlopen(req, context=context)
html = uClient.read()
uClient.close()
data = []

soup = BeautifulSoup(html, 'html.parser')

divofinterest = soup.find('div', class_='_3OXQ1 _26IxR _3bGVu')

for item in divofinterest.find_all('div', class_='_3bhpO'):
    url = item.find('a')['href']
    url = 'https://www.abc.net.au/news/justin' + url
    title = (item.find('h3').getText())
    description = (item.find('div',class_='_3P1Sq _1deB8 _1hGzz _1-RZJ _1yL-m').getText())

    data.append({
		'title':title,
		'url':url,
		'description':description
	})

datatowrite = pd.DataFrame(data)
datatowrite.to_csv('abcnews.csv',sep=';',index=False)
