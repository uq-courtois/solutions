### Exercise 1

# Read the data file http://www.digitalanalytics.id.au/static/files/billboard_merged.csv
# Aggregate this data into a new dataframe named grouped so you get the maximum danceability scores for each individual artist
# Sort that new dataframe named grouped on those danceability scores in descending order
# Print the 10 first observations

import pandas as pd

df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/billboard_merged.csv', sep=',')

grouped = df.groupby(['artist'], as_index=False)[['danceability']].max()

grouped = grouped.sort_values(by=['danceability'], ascending=False)

print(grouped.head(10))

### Exercise 2

# Read the data file http://www.digitalanalytics.id.au/static/files/billboard_merged.csv
# Describe the variable artist
# Get the mode of that variable (mode is category with highest frequency)

import pandas as pd
import researchpy as rp

df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/billboard_merged.csv', sep=',')

catsum = rp.summary_cat(df['artist'])
print(catsum)

### Exercise 3

# Fork code from: https://replit.com/@CedricCourtois/RegularKnowingAtoms#main.py
# Describe the variable popularitycat
# Get the median of that variable
# Visualize the distribution of the variable

import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt

df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/billboard_merged.csv',sep=',') 

def categorization(popularity):
	if popularity >= 50:
		popularitycat = 1
	else:
		popularitycat = 0
	return popularitycat

df['popularitycat'] = df['popularity'].apply(lambda x: categorization(x))

print('Median:',(df['popularitycat']).median())

# Optional > assigns string values instead of numeric labels
def categorization(popularity):
	if popularity >= 50:
		popularitycat = 'High popularity'
	else:
		popularitycat = 'Low popularity'
	return popularitycat

df['popularitycat'] = df['popularity'].apply(lambda x: categorization(x))

catsum = rp.summary_cat(df['popularitycat'])
print(catsum)

# BART CHART
plt.bar(catsum['Outcome'],catsum['Count'])
plt.tight_layout()
plt.savefig('popularitycat-absolute-barchart.pdf')
plt.clf() 

### Exercise 4

# Read the data file billboard_merged.csv

#Describe the variable danceability
#Get the mean and standard deviation of that variable
#Visualize the distribution of the variable

#Describe the variable acousticness
#Get the mean and standard deviation of that variable
#Visualize the distribution of the variable

import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt
 
df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/billboard_merged.csv',sep=',') 

print(df['danceability'].describe())
 
### HISTOGRAM
plt.hist(df['danceability'], bins=100)
plt.tight_layout()
plt.savefig('histo_danceability.pdf')
plt.clf() 

print(df['acousticness'].describe())
 
### HISTOGRAM
plt.hist(df['acousticness'], bins=100)
plt.tight_layout()
plt.savefig('histo_acousticness.pdf')
plt.clf() 

