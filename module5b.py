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

# Fork code from: https://replit.com/@ZoeMacLean/Week-10-Exercises
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

### Exercise 5
# Fork code from: https://replit.com/@ZoeMacLean/Week-10-Exercises
# Describe and visualize the relationship between the variables popularitycat and decade

import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt

df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/billboard_merged.csv',sep=',') 

def categorization(popularity):
	if popularity >= 50:
		popularitycat = 'High popularity'
	else:
		popularitycat = 'Low popularity'
	return popularitycat

df['popularitycat'] = df['popularity'].apply(lambda x: categorization(x))

def categorization(year):
	if year >= 1990 and year < 2000:
		decade = '1990s'
	if year >= 2000 and year < 2010:
		decade = '2000s'
	if year >= 2010:
		decade = '2010s'
	return decade
	
df['decade'] = df['year'].apply(lambda x: categorization(x))

# CROSSTABULATION
table, results = rp.crosstab(df['popularitycat'],df['decade'], prop= 'col', test= 'chi-square')
 
print(table) # Prints crosstab
print()
print(results) # Prints statistics tab
 
# STACKED BAR CHART
ct = pd.crosstab(df['decade'],df['popularitycat'],normalize='index') # Create PD crosstab as basis for plot
ct.plot.bar(stacked=True) # Generate plot
plt.legend(loc='lower left', bbox_to_anchor= (0.0, 1.01),frameon=False) # Tidy up legend (other)
plt.xticks(rotation="horizontal") # Horizontal x-axis labels
plt.xlabel('Decade') # Adding label on x-axis
plt.ylabel('Popularity') # Adding label on y-axis
plt.tight_layout() # Forces tidy plot lay-out
plt.savefig('stackedbar.pdf') # Saving figure
 
# Clear figure
plt.clf() 

### Exercise 6

# Read the data file http://www.digitalanalytics.id.au/static/files/billboard_merged.csv
# Describe and visualize the relationship between the variables popularity and danceability

import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt
 
df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/billboard_merged.csv', delimiter = ',') 
 
### CORRELATION
print(rp.correlation.corr_pair(df[['popularity', 'danceability']]))
 
### SCATTERPLOT
plt.scatter(df['popularity'],df['danceability']) # Build plot
plt.xlabel('Popularity') # x-axis label
plt.ylabel('Danceability') # y-axis label
plt.tight_layout() # Forces tidy plot lay-out
plt.savefig('scatterplot.pdf') # Save figure
plt.clf() # Clear figure

### Exercise 7

# Read the data file http://www.digitalanalytics.id.au/static/files/billboard_merged.csv
# Aggregate the dataset into a new dataframe named grouped so you get the standard deviation of danceability per year (year being the grouping variable)
# Add another variable: acousticness

import pandas as pd
 
df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/billboard_merged.csv', delimiter = ',') 
x = grouped.groupby(['year'], as_index=False)[['danceability','acousticness']].std()
print(x)

### Exercise 8

# Plot the relationship between the standard deviations of danceability and acousticness and year measures in the previously constructed dataframe named grouped (i.e., construct a time series graph)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/billboard_merged.csv', delimiter = ',') 

x = df.groupby(['year'], as_index=False)[['danceability','acousticness']].std()

print(x)

# Time series
plt.plot(x['year'],x['danceability'],label="Danceability")
plt.plot(x['year'],x['acousticness'],label="Accousticness")
plt.legend()
plt.tight_layout()
plt.savefig('timeseries.pdf')
plt.clf()
