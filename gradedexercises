### Graded exercise Module 1a (different versions, variations on same exercise)

# Define a list 'x' with the following integer values: 2,4,5,4,6
x = [2,4,5,4,6]

# Append the integer value 8
x.append(8)

# Print the last element of the list to the console
print(x[-1])

# Define a list of dictionaries that contains the info from the following table:
# Name	Income
# Lisa	3400
# Sam	2120
# Jasmine	1240

x = [
	{'Name':'Lisa','Income':3400},
	{'Name':'Sam','Income':2120},
	{'Name':'Jasmine','Income':1240},
]

# Change Jasmine's income to 2240
x[2]['Income'] = 2240

# Isolate and print Jasmine's updated income from the list of dicts
print(x[2]['Income'])

### Graded exercise Module 1b (different versions, variations on same exercise)

# Define a variable named ‘dataset’ that contains the following information:

# Artist	Track	Plays
# Dire Straits	Sultans of Swing	65
# Pink Floyd	Comfortably Numb	23
# The Smiths	Cemetery Gates	15
# Nick Cave & The Bad Seeds	The Ship Song	36
# Dire Straits	Brothers in Arms	20

dataset = [
	{'Artist':'Dire Straits','Track':'Sultans of Swing','Plays':65},
	{'Artist':'Pink Floyd','Track':'Comfortably Numb','Plays':23},
	{'Artist':'The Smiths','Track':'Cemetery Gates','Plays':15},
	{'Artist':'Nick Cave & The Bad Seeds','Track':'The Ship Song','Plays':36},
	{'Artist':'Dire Straits','Track':'Brothers in Arms','Plays':20},
]

# Print the artist and track (title) of songs with more than 20 plays. Each artist and track combination is printed on a separate line.

for d in dataset:
	if d['Plays'] > 20:
		print(d['Artist'],'-',d['Track'])

# Print all track titles of songs by Dire Straits and Pink Floyd. Printing just the titles is ok, each title is printed on a separate line.

for d in dataset:
	if 'Dire Straits' in d['Artist'] or 'Pink Floyd' in d['Artist']:
		print(d['Track'])

# Print the total number of plays. This is the total number of plays of all 5 songs.

x = []
for d in dataset:
	x.append(d['Plays'])

print(sum(x))

### Graded exercise Module 2 (different versions, variations on same exercise)

# Read in the file artistsong.csv (Available at http://digitalanalytics.id.au/static/files/artistsong.csv).

import pandas as pd
 
data = pd.read_csv('http://digitalanalytics.id.au/static/files/artistsong.csv',sep=';') # Reading data from csv
data = data.T.to_dict().values() # Converting dataframe into list of dictionaries
 
# Write the information of songs with 20 or more plays into a new file called artistsong_filtered.csv (i.e., artist, track, plays).

x = []
for d in data:
	if d['Plays'] >= 20:
		x.append(d)

newdata = pd.DataFrame(x)
newdata.to_csv('artistsong_filtered.csv',sep=';',index=False)
