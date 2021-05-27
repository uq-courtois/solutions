# Exercise 1

import pandas as pd
 
df1 = pd.read_csv('http://www.digitalanalytics.id.au/static/files/billboard1.csv',sep=',') 
df2 = pd.read_csv('http://www.digitalanalytics.id.au/static/files/billboard2.csv',sep=',')
 
print(df1.info())
print(df2.info())
 
df = df1.append(df2)

print(df.info())

df.to_csv('billboard.csv',sep=',',index=False) 

# Exercise 2

import pandas as pd
 
df1 = pd.read_csv('billboard.csv',sep=',')
df2 = pd.read_csv('http://www.digitalanalytics.id.au/static/files/billboard_additional.csv',sep=',')
 
print(df1.info()) # 4 variables, 19342 rows
print(df2.info()) # 6 variables, 19335 rows
 
df = pd.merge(df1, df2, how="left", on=['trackid'])
 
print(df.info()) 
df.to_csv('billboard_merged.csv',sep=',',index=False) 

# Exercise 3

import pandas as pd

df = pd.read_csv('billboard_merged.csv',sep=',') 

grouped = df.groupby(['artist'], as_index=False)[['danceability']].sum()
 
grouped = grouped.sort_values(by=['danceability'], ascending=False)

print(grouped.head(10))

# Exercise 4

import pandas as pd
import researchpy as rp

df = pd.read_csv('billboard_merged.csv',sep=',') 

print(df.info()) 

print(df['artist'].unique())
print(len(df['artist'].unique()))
catsum = rp.summary_cat(df['artist'])
print(catsum)

# Exercise 5

import pandas as pd
import researchpy as rp

df = pd.read_csv('billboard_merged.csv',sep=',') 

def popularityf(x):
	if x < 33:
		popularity = 1
	if x >= 33 and x < 66:
		popularity = 2
	if x >= 66:
		popularity = 3

	return popularity

df['popularitycat'] = df['popularity'].apply(lambda x: popularityf(x))

print(df.info()) 

print(df['popularitycat'].unique())
print(len(df['popularitycat'].unique()))
catsum = rp.summary_cat(df['popularitycat'])
print(catsum)

print('Median:',(df['popularitycat']).median())

# Exercise 6

import pandas as pd

df = pd.read_csv('billboard_merged.csv',sep=',') 

print(df.info()) 

print(df['danceability'].unique())
print(len(df['danceability'].unique()))

print(df['danceability'].describe())

# Exercise 7

import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt

df = pd.read_csv('billboard_merged.csv',sep=',')

def decadef(x):
	if x >= 1990 and x < 2000:
		decade = '1990s'
	if x >= 2000 and x < 2010:
		decade = '2000s'
	if x >= 2010 and x < 2020:
		decade = '2010s'
	if x >= 2020:
		decade = '2020s'
	
	return decade

df['decade'] = df['year'].apply(lambda x: decadef(x))

def popularityf(x):
	if x < 33:
		popularity = '1. Low popularity'
	if x >= 33 and x < 66:
		popularity = '2. Medium popularity'
	if x >= 66:
		popularity = '3. High popularity'

	return popularity

df['popularitycat'] = df['popularity'].apply(lambda x: popularityf(x))

print(df.info()) 

# CROSSTABULATION
table, results = rp.crosstab(df['decade'],df['popularitycat'], prop= 'col', test= 'chi-square')
 
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
plt.tight_layout() # Forces tidy plot lay-out – a life saver!
plt.savefig('stackedbar.pdf') # Saving figure
plt.clf() # Clearing figure

# Exercise 8

import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt

df = pd.read_csv('billboard_merged.csv',sep=',')

### CORRELATION
print(rp.correlation.corr_pair(df[['popularity', 'danceability']]))
 
# The r-value is the magnitude of the correlation
# p-value expresses statistical significance level
# N reports number of cases the analysis is based on
 
### SCATTERPLOT
plt.scatter(df['popularity'],df['danceability']) # Build plot
plt.xlabel('Popularity') # x-axis label
plt.ylabel('Dancebility') # y-axis label
plt.savefig('scatterplot.pdf') # Save figure
plt.clf() # Clear figure

# Exercise 9 and 10

import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt

df = pd.read_csv('billboard_merged.csv',sep=',')

# Build aggregated dataframe
grouped = df.groupby(['year'], as_index=False)[['danceability','acousticness']].std()

print(grouped)

plt.plot(grouped['year'],grouped['danceability'],label="Danceability")
plt.plot(grouped['year'],grouped['acousticness'],label="Acousticness")

plt.legend() # Add a legend
plt.savefig('timeseries.pdf') # Save the figure
plt.clf() # Clear figure

### CORRELATION
print(rp.correlation.corr_pair(grouped[['year', 'danceability']]))
print(rp.correlation.corr_pair(grouped[['year', 'acousticness']]))
