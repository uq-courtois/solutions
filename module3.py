### Exercise 1: 
#Print all the HTML of https://digitalanalytics.id.au/static/materials/9gag/  in the console

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

soup = scraper('https://digitalanalytics.id.au/static/materials/9gag')
print(soup) # Print all HTML

### Exercise 2:
#Open https://digitalanalytics.id.au/static/materials/9gag/  in Firefox or Chrome
#Locate the HTML object that contains the text ‘9Gag Hot Section’
# Print the text of this HTML object in the console

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

soup = scraper('https://digitalanalytics.id.au/static/materials/9gag')

title = soup.find('h1').getText()
print(title)

### Exercise 3
#Open https://digitalanalytics.id.au/static/materials/9gag/  in Firefox or Chrome
#Locate the HTML object that contains the link ‘Upload a meme’
# Print the URL this link directs to in the console

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

soup = scraper('https://digitalanalytics.id.au/static/materials/9gag')

url = soup.find('a')['href']
print(url)

### Exercise 4
# Open https://digitalanalytics.id.au/static/materials/9gag/  in Firefox or Chrome
# Print the text of all the meme titles to the console (i.e., ‘History Lesson’, ‘See you in a few weeks’,…)

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

soup = scraper('https://digitalanalytics.id.au/static/materials/9gag')

for i in soup.find_all('h2'):
	print(i.getText())

### Exercise 5
# Open https://digitalanalytics.id.au/static/materials/9gag/  in Firefox or Chrome
# Print the source URLs of all the meme images in the console (i.e., https://img-9gag-fun.9cache.com/photo/ang2vYq_460s.jpg, https://img-9gag-fun.9cache.com/photo/azeKZpb_460s.jpg,...)

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

soup = scraper('https://digitalanalytics.id.au/static/materials/9gag')

for i in soup.find_all('img'):
	print(i['src'])

### Exercise 6
# Open https://digitalanalytics.id.au/static/materials/9gag/  in Firefox or Chrome
# Download all the images to your Replit

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

soup = scraper('https://digitalanalytics.id.au/static/materials/9gag')

for i in soup.find_all('img'):
	imgurl = i['src']
	print(imgurl)
	
	filename = imgurl.split('/')[-1]
	
	imgfile = open(filename,'wb') 
	imgfile.write(urlopen(imgurl).read())
	imgfile.close() 

### Exercise 7
# Open https://digitalanalytics.id.au/static/materials/9gag/  in Firefox or Chrome
# Print each combination of meme title and image URL to the console

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

soup = scraper('https://digitalanalytics.id.au/static/materials/9gag')

for i in soup.find_all('div',class_='post'):
	title = i.find('h2').getText()
	print(title)
	imgurl = i.find('img')['src']
	print(imgurl)

# BIS: save the info scraped in Exercise 7 to a file

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import pandas as pd

def scraper(url):
 
	headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	req = Request(url, headers=headers)
	context = ssl._create_unverified_context()
	
	uClient= urlopen(req, context=context)
	html = uClient.read()
	uClient.close()
 
	return BeautifulSoup(html, 'html.parser')

soup = scraper('https://digitalanalytics.id.au/static/materials/9gag')

data = []

for i in soup.find_all('div',class_='post'):
	title = i.find('h2').getText()
	print(title)
	imgurl = i.find('img')['src']
	print(imgurl)

	data.append({
		'title':title,
		'imgurl':imgurl,
	})

newdata = pd.DataFrame(data)
newdata.to_csv('9gag.csv',sep=',',index=False)
