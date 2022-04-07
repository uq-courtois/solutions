### Exercise 1
# Print all the HTML from
# https://digitalanalytics.id.au/static/materials/9gagreal/

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
def scraper(url):
 
	headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	req = Request(url, headers=headers)
	context = ssl._create_unverified_context()
	
	uClient= urlopen(req, context=context)
	html = uClient.read()
	uClient.close()
 
	return BeautifulSoup(html, 'html.parser')

# WARNING: CHANGE THE URL ON THE NEXT LINE INTO THE URL OF THE PAGE YOU AIM TO SCRAPE
soup = scraper('https://digitalanalytics.id.au/static/materials/9gagreal/')

print(soup)

### Exercise 2
# Print the text of the meme title from 
# https://digitalanalytics.id.au/static/materials/9gagreal/

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
def scraper(url):
 
	headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	req = Request(url, headers=headers)
	context = ssl._create_unverified_context()
	
	uClient= urlopen(req, context=context)
	html = uClient.read()
	uClient.close()
 
	return BeautifulSoup(html, 'html.parser')

# WARNING: CHANGE THE URL ON THE NEXT LINE INTO THE URL OF THE PAGE YOU AIM TO SCRAPE
soup = scraper('https://digitalanalytics.id.au/static/materials/9gagreal/')

title = soup.find('h1').getText()
print(title)

### Exercise 3
# Print the number of comments on the meme from 
# https://digitalanalytics.id.au/static/materials/9gagreal/

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
def scraper(url):
 
	headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	req = Request(url, headers=headers)
	context = ssl._create_unverified_context()
	
	uClient= urlopen(req, context=context)
	html = uClient.read()
	uClient.close()
 
	return BeautifulSoup(html, 'html.parser')

# WARNING: CHANGE THE URL ON THE NEXT LINE INTO THE URL OF THE PAGE YOU AIM TO SCRAPE
soup = scraper('https://digitalanalytics.id.au/static/materials/9gagreal/')

comments = soup.find('span',class_='comment-tab-bar__label').getText()
print(comments)

### Exercise 4
# Download the meme image from
# https://digitalanalytics.id.au/static/materials/9gagreal/

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
def scraper(url):
 
	headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	req = Request(url, headers=headers)
	context = ssl._create_unverified_context()
	
	uClient= urlopen(req, context=context)
	html = uClient.read()
	uClient.close()
 
	return BeautifulSoup(html, 'html.parser')

# WARNING: CHANGE THE URL ON THE NEXT LINE INTO THE URL OF THE PAGE YOU AIM TO SCRAPE
soup = scraper('https://digitalanalytics.id.au/static/materials/9gagreal/')

div = soup.find('div',class_='image-post post-view')
imgurl = 'https://digitalanalytics.id.au/static/materials/9gagreal/' + div.find('img')['src']
print(imgurl)

# Copy/paste from shortcuts
filename = imgurl.split('/')[-1]
imgfile = open(filename,'wb') 
imgfile.write(urlopen(imgurl).read())
imgfile.close() 
	
### Exercise 5
# Get the HTML from
# https://digitalanalytics.id.au/static/materials/9gagreal2/
# Get all the tags and store them in a list
# Print the list with tags at the end of your script

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
def scraper(url):
 
	headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	req = Request(url, headers=headers)
	context = ssl._create_unverified_context()
	
	uClient= urlopen(req, context=context)
	html = uClient.read()
	uClient.close()
 
	return BeautifulSoup(html, 'html.parser')

# WARNING: CHANGE THE URL ON THE NEXT LINE INTO THE URL OF THE PAGE YOU AIM TO SCRAPE
soup = scraper('https://digitalanalytics.id.au/static/materials/9gagreal2/')

tags = []

div = soup.find('div',class_='post-tag')
for i in div.find_all('a'):
	tag = i.getText()
	tags.append(tag)

print(tags)

### Exercise 6
# Get the video URL from
# https://digitalanalytics.id.au/static/materials/9gagreal2/

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
def scraper(url):
 
	headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	req = Request(url, headers=headers)
	context = ssl._create_unverified_context()
	
	uClient= urlopen(req, context=context)
	html = uClient.read()
	uClient.close()
 
	return BeautifulSoup(html, 'html.parser')

# WARNING: CHANGE THE URL ON THE NEXT LINE INTO THE URL OF THE PAGE YOU AIM TO SCRAPE
soup = scraper('https://digitalanalytics.id.au/static/materials/9gagreal2/')

div = soup.find('div',class_='post-view video-post')
video = 'https://digitalanalytics.id.au/static/materials/9gagreal2/' + div.find('source')['src']
print(video)

### Exercise 7
# Get the HTML from
# https://www.alexa.com/topsites/countries
# Get all the country URLs and store them in a list
# Print the list with URLs at the end of your script

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
def scraper(url):
 
	headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	req = Request(url, headers=headers)
	context = ssl._create_unverified_context()
	
	uClient= urlopen(req, context=context)
	html = uClient.read()
	uClient.close()
 
	return BeautifulSoup(html, 'html.parser')

urls = []

soup = scraper('https://www.alexa.com/topsites/countries')

for i in soup.find_all('a'):
	if 'countries/' in i['href']:
		url = 'https://www.alexa.com/topsites/' + i['href']
		print(url)
		urls.append(url)
		
### Exercise 8
# Get the HTML from
# https://www.alexa.com/topsites/countries/AL
# Create a list of dictionaries with the keys 'Website' and 'Rank'

		from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
def scraper(url):
 
	headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	req = Request(url, headers=headers)
	context = ssl._create_unverified_context()
	
	uClient= urlopen(req, context=context)
	html = uClient.read()
	uClient.close()
 
	return BeautifulSoup(html, 'html.parser')

data = []

soup = scraper('https://www.alexa.com/topsites/countries/AL')

rank = 0

for i in soup.find_all('a'):
	if '/siteinfo/' in i['href']:
		rank += 1
		print(rank,i.getText())

		data.append({
			'Rank':rank,
			'Website':i.getText(),
		})

### MULTIPAGE SCRAPER

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import time
import pandas as pd

def scraper(url):
 
	headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	req = Request(url, headers=headers)
	context = ssl._create_unverified_context()
	
	uClient= urlopen(req, context=context)
	html = uClient.read()
	uClient.close()
 
	return BeautifulSoup(html, 'html.parser')

urls = []

soup = scraper('https://www.alexa.com/topsites/countries')

for i in soup.find_all('a'):
	if 'countries/' in i['href']:
		url = 'https://www.alexa.com/topsites/' + i['href']
		print(url)
		urls.append(url)

data = []

for url in urls:

	print(url)

	soup = scraper(url)

	rank = 0

	for i in soup.find_all('a'):
		if '/siteinfo/' in i['href']:
			rank += 1
			print(rank,i.getText())
	
			data.append({
				'Country':url.split('/')[-1],
				'Rank':rank,
				'Website':i.getText(),
			})
	
	time.sleep(2)
	
	newdata = pd.DataFrame(data)
	newdata.to_csv('alexa.csv',sep=',',index=False)
