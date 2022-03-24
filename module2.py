### Exercise 1
# Read file
# https://digitalanalytics.id.au/static/files/insta.csv
# Loop through each entry in the data and print it

import pandas as pd # import pandas module, once at the top of the script
 
data = pd.read_csv('https://digitalanalytics.id.au/static/files/insta.csv',sep=',')
data = data.T.to_dict().values()

for d in data:
	print(d)

### Exercise 2
# In followers: replace K with 000 and M with 000000

import pandas as pd # import pandas module, once at the top of the script
 
data = pd.read_csv('https://digitalanalytics.id.au/static/files/insta.csv',sep=',')
data = data.T.to_dict().values()

for d in data:
	d['followers'] = d['followers'].replace('K','000')
	d['followers'] = d['followers'].replace('M','000000')
	d['followers'] = int(d['followers'])
	print(['account'],d['followers'])


### Exercise 3
# Only print account names with a million or more followers

import pandas as pd # import pandas module, once at the top of the script
 
data = pd.read_csv('https://digitalanalytics.id.au/static/files/insta.csv',sep=',')
data = data.T.to_dict().values()

for d in data:
	d['followers'] = d['followers'].replace('K','000')
	d['followers'] = d['followers'].replace('M','000000')
	d['followers'] = int(d['followers'])

	if d['followers'] >= 1000000:
		print(['account'],d['followers'])


### Exercise 4
# Only print account names with a follower count between 2000 and 6000

import pandas as pd # import pandas module, once at the top of the script
 
data = pd.read_csv('https://digitalanalytics.id.au/static/files/insta.csv',sep=',')
data = data.T.to_dict().values()

for d in data:
	d['followers'] = d['followers'].replace('K','000')
	d['followers'] = d['followers'].replace('M','000000')
	d['followers'] = int(d['followers'])

	if d['followers'] > 2000 and d['followers'] < 6000 :
		print(['account'],d['followers'])

### Exercise 5
# Save the processed information to a file in your replit named insta_processed.csv

import pandas as pd # import pandas module, once at the top of the script
 
data = pd.read_csv('https://digitalanalytics.id.au/static/files/insta.csv',sep=',')
data = data.T.to_dict().values()

for d in data:
	d['followers'] = d['followers'].replace('K','000')
	d['followers'] = d['followers'].replace('M','000000')
	d['followers'] = int(d['followers'])

data = pd.DataFrame(data)
data.to_csv('insta_processed.csv',sep=',',index=False)

### Exercise 6
# Loop through each entry in the data and print it

import pandas as pd # import pandas module, once at the top of the script
 
data = pd.read_csv('https://digitalanalytics.id.au/static/files/youtube.csv',sep=',')
data = data.T.to_dict().values()

for d in data:
	print(d)

### Exercise 7
# Calculate the ratio of likes versus dislikes (likes divided by dislikes) for each entry and print this value

import pandas as pd # import pandas module, once at the top of the script
 
data = pd.read_csv('https://digitalanalytics.id.au/static/files/youtube.csv',sep=',')
data = data.T.to_dict().values()

for d in data:
	print(d['likes']/d['dislikes'])

### Exercise 8
# Calculate the ratio of likes versus dislikes (likes divided by dislikes) for each entry and add this value to the dictionary in the key ['ratio']
# Print the key ['ratio']
# Write the data into a file youtube_update.csv

import pandas as pd # import pandas module, once at the top of the script
 
data = pd.read_csv('https://digitalanalytics.id.au/static/files/youtube.csv',sep=',')
data = data.T.to_dict().values()

for d in data:
	d['ratio'] = d['likes']/d['dislikes']
	print(d['ratio'])

data = pd.DataFrame(data)
data.to_csv('youtube_update.csv',sep=',',index=False)

### Exercise 9
# Define a string variable x with the value 'This day is bananas'
# Write a program that generates the following output (NO HARDCODING)

# This day is bananas
# b
# a
# n
# a
# n
# a
# s

x = 'This day is bananas'
print(x)
for d in x.split(' ')[-1]:
	print(d)

### Exercise 10
# Read file
# https://digitalanalytics.id.au/static/files/vevo_tutorial.csv
# Only print dictionaries that contain information from videos from Ariana Grande's orJustin Bieber's channel
# ArianaGrandeVevo - justintimberlakeVEVO

import pandas as pd # import pandas module, once at the top of the script
 
data = pd.read_csv('https://digitalanalytics.id.au/static/files/vevo_tutorial.csv',sep=',')
data = data.T.to_dict().values()

for d in data:
	if d['artist'] == 'ArianaGrandeVevo' or d['artist'] == 'justintimberlakeVEVO':
		print(d)

### Exercise 11
# Only print the titles of videos that were viewed over 200000 times

import pandas as pd # import pandas module, once at the top of the script
 
data = pd.read_csv('https://digitalanalytics.id.au/static/files/vevo_tutorial.csv',sep=',')
data = data.T.to_dict().values()

for d in data:
	if d['views'] > 200000:
		print(d['title'])

### Exercise 12
# Calculate the mean number of views for all videos in the file

import pandas as pd # import pandas module, once at the top of the script
 
data = pd.read_csv('https://digitalanalytics.id.au/static/files/vevo_tutorial.csv',sep=',')
data = data.T.to_dict().values()
views = []

for d in data:
	views.append(d['views'])

print(sum(views)/len(views))

### Exercise 13
# The valid url for a YouTube video is the base url plus the video ID from our csv file. Overwrite the url key with a valid url for each video.
# https://www.youtube.com/watch?v=
# Save the updated list of dictionaries to a new file youtube_clean.csv

import pandas as pd # import pandas module, once at the top of the script
 
data = pd.read_csv('https://digitalanalytics.id.au/static/files/vevo_tutorial.csv',sep=',')
data = data.T.to_dict().values()

for d in data:
	d['url'] = 'https://www.youtube.com/watch?v='+d['url']

data = pd.DataFrame(data)
data.to_csv('youtube_clean.csv',sep=',',index=False)
