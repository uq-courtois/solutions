### Module 3 - Scraping

# Exercise 1

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
# The URL we want to scrape
url = 'https://en.wikipedia.org/wiki/Mark_Wahlberg'
 
#################################################
#################################################
### COPY/PASTE THIS BLOCK AS IS
 
# Open URL (i.e., make request) + disguise agent
headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = Request(url, headers=headers)
context = ssl._create_unverified_context()
 
# To fetch html and store in variable 'html'
uClient= urlopen(req, context=context)
html = uClient.read() # html is stored in variable html
uClient.close()
 
#################################################
#################################################
 
### Interpret the page source as html
soup = BeautifulSoup(html, 'html.parser')

articletext = soup.find('div',class_='mw-parser-output').getText()
print(articletext)
open("article.txt", "w", encoding='utf8').write(articletext)

# Exercise 2

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
# The URL we want to scrape
url = 'https://www.abc.net.au/news/2021-03-16/facebook-users-switching-off-due-to-boredom/13248184'
 
#################################################
#################################################
### COPY/PASTE THIS BLOCK AS IS
 
# Open URL (i.e., make request) + disguise agent
headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = Request(url, headers=headers)
context = ssl._create_unverified_context()
 
# To fetch html and store in variable 'html'
uClient= urlopen(req, context=context)
html = uClient.read() # html is stored in variable html
uClient.close()
 
#################################################
#################################################
 
### Interpret the page source as html
soup = BeautifulSoup(html, 'html.parser')

imgdiv = soup.find('div',class_='lt7xz')
imgurl = imgdiv.find('img')['data-src'].split('?')[0]
print(imgurl)

imgfile = open('image.jpg','wb')
imgfile.write(urlopen(imgurl).read())
imgfile.close()

# Exercise 3

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
# The URL we want to scrape
url = 'https://www.allmusic.com/newreleases'
 
#################################################
#################################################
### COPY/PASTE THIS BLOCK AS IS
 
# Open URL (i.e., make request) + disguise agent
headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = Request(url, headers=headers)
context = ssl._create_unverified_context()
 
# To fetch html and store in variable 'html'
uClient= urlopen(req, context=context)
html = uClient.read() # html is stored in variable html
uClient.close()
 
#################################################
#################################################
 
### Interpret the page source as html
soup = BeautifulSoup(html, 'html.parser')

for i in soup.find_all('div',class_='title'):
	print(i.find('a').getText())
	
# Exercise 4

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
# The URL we want to scrape
url = 'https://www.allmusic.com/newreleases'
 
#################################################
#################################################
### COPY/PASTE THIS BLOCK AS IS
 
# Open URL (i.e., make request) + disguise agent
headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = Request(url, headers=headers)
context = ssl._create_unverified_context()
 
# To fetch html and store in variable 'html'
uClient= urlopen(req, context=context)
html = uClient.read() # html is stored in variable html
uClient.close()
 
#################################################
#################################################
 
### Interpret the page source as html
soup = BeautifulSoup(html, 'html.parser')

for i in soup.find_all('div',class_='meta-container'):
	artist = i.find('div',class_='artist').getText().strip()
	titlediv = i.find('div',class_='title')
	title = titlediv.getText().strip()
	url = titlediv.find('a')['href']
	
	print(artist,'-',title)
	print(url)
	print()
	
# Exercise 5

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import pandas as pd
 
# The URL we want to scrape
url = 'https://www.allmusic.com/newreleases'
 
#################################################
#################################################
### COPY/PASTE THIS BLOCK AS IS
 
# Open URL (i.e., make request) + disguise agent
headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = Request(url, headers=headers)
context = ssl._create_unverified_context()
 
# To fetch html and store in variable 'html'
uClient= urlopen(req, context=context)
html = uClient.read() # html is stored in variable html
uClient.close()
 
#################################################
#################################################
 
### Interpret the page source as html
soup = BeautifulSoup(html, 'html.parser')

x = []

for i in soup.find_all('div',class_='meta-container'):
	artist = i.find('div',class_='artist').getText().strip()
	titlediv = i.find('div',class_='title')
	title = titlediv.getText().strip()
	url = titlediv.find('a')['href']

	print(artist,'-',title)
	print(url)
	print()

	x.append({
		'artist':artist,
		'title':title,
		'url':url
	})

x = pd.DataFrame(x)
x.to_csv('allmusic.csv',sep=';',index=False)
