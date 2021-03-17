# Tutorial Module 2

# Exercise 1

import pandas as pd
 
data = pd.read_csv('https://www.digitalanalytics.id.au/static/files/youtube_vevo.csv',sep=';') 
data = data.T.to_dict().values()

for item in data:
	print(item)

data = pd.DataFrame(data) 
data.to_csv('vevo_tutorial.csv',sep=';',index=False)

# Exercise 2

import pandas as pd
 
data = pd.read_csv('vevo_tutorial.csv',sep=';') 
data = data.T.to_dict().values()

for item in data:
	if item['artist'] == 'ArianaGrandeVevo' or item['artist'] == 'JustinBieberVEVO':
		print(item)

# Exercise 3

import pandas as pd
 
data = pd.read_csv('vevo_tutorial.csv',sep=';') 
data = data.T.to_dict().values()

for item in data:
	if item['views'] > 200000:
		print(item)

# Exercise 4

import pandas as pd

data = pd.read_csv('vevo_tutorial.csv',sep=';') 
data = data.T.to_dict().values()

for item in data:
	if 'live' in item['title'].lower():
		print(item)

# Exercise 4bis - Version based on Regular Expressions (regex), to avoid false negatives such as 'Alive' as'live': only live as it is not a part of a larger word
# More on regex: https://www.youtube.com/watch?v=sa-TUpSx1JA

import pandas as pd
import re

data = pd.read_csv('vevo_tutorial.csv',sep=';') 
data = data.T.to_dict().values()

for item in data:
	if re.match('\blive\b', item['title'].lower()):
			print(item)

# Exercise 5

import pandas as pd
 
data = pd.read_csv('vevo_tutorial.csv',sep=';') 
data = data.T.to_dict().values()

x = []

for item in data:
	if item['views'] > 200000:
		print(item)
		x.append(item)

x = pd.DataFrame(x) 
x.to_csv('youtube_over200k.csv',sep=';',index=False)

# Exercise 6

import pandas as pd
 
data = pd.read_csv('vevo_tutorial.csv',sep=';') 
data = data.T.to_dict().values()

x = []

for item in data:
	item['url'] = 'https://www.youtube.com/watch?v='+item['url']
	x.append(item)

x = pd.DataFrame(x) 
x.to_csv('youtube_over200k.csv',sep=';',index=False)

# Exercise 7

import pandas as pd
 
data = pd.read_csv('vevo_tutorial.csv',sep=';') 
data = data.T.to_dict().values()

x = []

for item in data:
	x.append(item['artist'])

x = list(set(x))
x.sort()

print(x)
print(len(x))

# Exercise 8

import pandas as pd
 
data = pd.read_csv('vevo_tutorial.csv',sep=';') 
data = data.T.to_dict().values()

x = []

for item in data:
	if 'jennifer lopez' not in item['title'].lower():
		x.append(item)

data = pd.read_csv('vevo_tutorial.csv',sep=';') 
data = data.T.to_dict().values()
