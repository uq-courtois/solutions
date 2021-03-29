# Tutorial 6 - Scraping pt. 2

# Exercise 1 - Wikipedia code

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
url = 'https://en.wikipedia.org/w/index.php?title=Special:Search&limit=100&offset=0&ns0=1&sort=last_edit_desc&sort=last_edit_desc&search=brisbane&advancedSearch-current=%7B%7D' 
 
headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = Request(url, headers=headers)
context = ssl._create_unverified_context()
 
uClient= urlopen(req, context=context)
html = uClient.read()
uClient.close()
 
soup = BeautifulSoup(html, 'html.parser')
searchresultdiv = soup.find('div',class_="searchresults mw-searchresults-has-iw")

searchresults = []

for i in searchresultdiv.find_all('div',class_='mw-search-result-heading'):
	searchresult = 'http://www.wikipedia.com'+i.find('a')['href']
	searchresults.append(searchresult)
	print(searchresult)
	
# Exercise 2 - Not available beyond tutorial
# Exercise 3 - Not available beyond tutorial

# Exercise 4

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
url = 'https://www.allmusic.com/blog/features' 
 
headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = Request(url, headers=headers)
context = ssl._create_unverified_context()
 
uClient= urlopen(req, context=context)
html = uClient.read()
uClient.close()
 
soup = BeautifulSoup(html, 'html.parser')
recentarticles = soup.find('div',class_='recent-article-container')

for i in recentarticles.find_all('div',class_='recent-article'):
	imgurl = i.find('img')['src']
	print(imgurl)

	# Use file name of original image
	imgfile = open(imgurl.split('/')[-1],'wb')
	imgfile.write(urlopen(imgurl).read())
	imgfile.close()
	
# Exercise 5

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
url = 'https://www.alexa.com/topsites/countries' 
 
headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = Request(url, headers=headers)
context = ssl._create_unverified_context()
 
uClient= urlopen(req, context=context)
html = uClient.read()
uClient.close()
 
soup = BeautifulSoup(html, 'html.parser')
tablecontainer = soup.find('div',class_='tableContainer')

urls = []

for i in tablecontainer.find_all('li'):
	url = 'https://www.alexa.com/topsites/'+i.find('a')['href']
	print(url)
	urls.append(url)

print('Harvested',len(urls),'country URLs')

# Exercise 6

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
url = 'https://www.alexa.com/topsites/countries/AL' 
 
headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = Request(url, headers=headers)
context = ssl._create_unverified_context()
 
uClient= urlopen(req, context=context)
html = uClient.read()
uClient.close()
 
soup = BeautifulSoup(html, 'html.parser')
tablecontainer = soup.find('div',class_='tableContainer')

for i in soup.find_all('div',class_='tr site-listing'):
	rowinfo = i.find_all('div',class_='td')
	rank = rowinfo[0].getText().strip()
	domain = rowinfo[1].getText().strip()
	country = url.split('/')[-1]
	print(country,rank,domain)
	
# Exercise 7

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import pause
import pandas as pd
 
url = 'https://www.alexa.com/topsites/countries' 

data = []

headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = Request(url, headers=headers)
context = ssl._create_unverified_context()
 
uClient= urlopen(req, context=context)
html = uClient.read()
uClient.close()
 
soup = BeautifulSoup(html, 'html.parser')
tablecontainer = soup.find('div',class_='tableContainer')

urls = []

for i in tablecontainer.find_all('li'):
	url = 'https://www.alexa.com/topsites/'+i.find('a')['href']
	print(url)
	urls.append(url)

print('Harvested',len(urls),'country URLs')

pause.seconds(3)

for url in urls:

	print('Scraping',url)
 
	headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	req = Request(url, headers=headers)
	context = ssl._create_unverified_context()
	
	uClient= urlopen(req, context=context)
	html = uClient.read()
	uClient.close()
	
	soup = BeautifulSoup(html, 'html.parser')
	tablecontainer = soup.find('div',class_='tableContainer')
	
	for i in soup.find_all('div',class_='tr site-listing'):
		rowinfo = i.find_all('div',class_='td')
		rank = rowinfo[0].getText().strip()
		domain = rowinfo[1].getText().strip()
		country = url.split('/')[-1]
		print(country,rank,domain)

		data.append({
			'country':country,
			'rank':rank,
			'domain':domain,
		})

data = pd.DataFrame(data) 
data.to_csv('alexa.csv',sep=',',index=False)

# Exercise 8

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
 
url = 'https://en.wikipedia.org/w/index.php?title=Special:Search&limit=100&offset=0&ns0=1&sort=last_edit_desc&sort=last_edit_desc&search=brisbane&advancedSearch-current=%7B%7D' 
 
headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = Request(url, headers=headers)
context = ssl._create_unverified_context()
 
uClient= urlopen(req, context=context)
html = uClient.read()
uClient.close()
 
soup = BeautifulSoup(html, 'html.parser')
searchresultdiv = soup.find('div',class_="searchresults mw-searchresults-has-iw")

searchresults = []

for i in searchresultdiv.find_all('div',class_='mw-search-result-heading'):
	searchresult = 'http://www.wikipedia.com'+i.find('a')['href']
	searchresults.append(searchresult)
	print(searchresult)

for url in searchresults:

	headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	req = Request(url, headers=headers)
	context = ssl._create_unverified_context()
	
	uClient= urlopen(req, context=context)
	html = uClient.read()
	uClient.close()

	soup = BeautifulSoup(html, 'html.parser')

	articletitle = soup.find('h1',class_='firstHeading').getText()
	articletext = soup.find('div',class_='mw-parser-output').getText()
	print(articletext)
	open(articletitle+".txt", "w", encoding='utf8').write(articletext)
