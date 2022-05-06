### Exercise 1

# Read data from file: https://digitalanalytics.id.au/static/files/spex_1.csv
# How many variables are there in the dataframe?
# How many observations are there in the dataframe?
# Print the first 15 values of the variable original_track
# Print the unique values in the variable original_artist
# How many unique values are there in the variable original_artist?

import pandas as pd

df = pd.read_csv('https://digitalanalytics.id.au/static/files/spex_1.csv', sep=',')
print(df.info())
print(df['original_track'].unique())
print(len(df['original_track'].unique()))

### Exercise 2

# Read data from file: http://www.digitalanalytics.id.au/static/files/spex_1.csv
# Define a subset of observations in variable df_sub if the value of the variable original_artist equals the string value 'Dire Straits’
# How many observations are there in the subset?
# How many unique recommended artists are there in the subset? 

import pandas as pd

df = pd.read_csv('https://digitalanalytics.id.au/static/files/spex_1.csv', sep=',')
df_sub = df[df['original_artist'] == 'Dire Straits']
print(df_sub.info())
print(len(df_sub['original_track'].unique()))

### Exercise 3

# Read data from file: http://www.digitalanalytics.id.au/static/files/spex_1.csv
# How many exact duplicates are there in the dataframe?
# What are the duplicates values?
# Remove the exact duplicates from the dataframe and print the shape of the dataframe

import pandas as pd
df = pd.read_csv('https://digitalanalytics.id.au/static/files/spex_1.csv', sep=',')

# Print number of exact duplicates
print('\n# Exact duplicates:', df.duplicated().sum())
# Print rows with duplicates
print('\nRows with duplicates:\n', df[df.duplicated()])
# Drop exact duplicates
df = df.drop_duplicates()

print(df.shape)

### Exercise 4

# Read data from file: http://www.digitalanalytics.id.au/static/files/spex_1.csv
# How many variables are there with missing values?
# How many rows with missing values doe we have?
# Remove the rows with missing values from the dataframe and print the shape of the dataframe

import pandas as pd
df = pd.read_csv('https://digitalanalytics.id.au/static/files/spex_1.csv', sep=',')

# Get summary of variables' missing data count
print('\n # Missing data:\n', df.isnull().sum())
# Print rows with missing data (add variable you want to inspect - here 'Song')
isolatemissing = pd.isnull(df['tempo'])
print('\n Rows with missing data:\n', df[isolatemissing])
# Drop rows with at least one missing value
df = df.dropna()

print(df.shape)

### Exercise 5
# Read data from file: http://www.digitalanalytics.id.au/static/files/spex_1.csv
# Create a new variable pinkfloyd in the dataframe. Assign value 1 if the value of original_artist equals 'Pink Floyd'. In all other cases, the value should be 0
# Print the first 40 values of the variables original_artist and pinkfloyd in the dataframe, side-by-side  

import pandas as pd
df = pd.read_csv('https://digitalanalytics.id.au/static/files/spex_1.csv', sep=',')

def categorisation(original_artist):
	if original_artist == 'Pink Floyd':
		pinkfloyd = 1
	else:
		pinkfloyd = 0
	return pinkfloyd
 
df['pinkfloyd'] = df['original_artist'].apply(lambda x: categorisation(x))
 
print(df[['original_artist','pinkfloyd']].head(40))

### Exercise 6

# Read data from file: http://www.digitalanalytics.id.au/static/files/spex_6.csv
# Create a new variable tempocat in the dataframe. Assign values:
# 1 if the value of tempo equals to or is smaller than 90
# 2 if the value of tempo is between 90 and 120
# 3 if the value of tempo equals 120 or more
# Print the first 40 values of the variables tempo and tempocat in the dataframe, side by side  

import pandas as pd
df = pd.read_csv('https://digitalanalytics.id.au/static/files/spex_6.csv', sep=',')

def categorisation(tempo):
	if tempo <= 90:
		tempocat = 1
	if tempo > 90 and tempo < 120:
		tempocat = 2
	if tempo >= 120:
		tempocat = 3
	return tempocat
	
df['tempocat'] = df['tempo'].apply(lambda x: categorisation(x))
 
print(df[['tempo','tempocat']].head(40))

### Exercise 7

# Read data files:
# http://www.digitalanalytics.id.au/static/files/spex_2.csv
# http://www.digitalanalytics.id.au/static/files/spex_3.csv
# Explore the files
# Combine them

import pandas as pd # import once at the top of your script
 
df1 = pd.read_csv('http://www.digitalanalytics.id.au/static/files/spex_2.csv',sep=',') # Read file 1
df2 = pd.read_csv('http://www.digitalanalytics.id.au/static/files/spex_3.csv',sep=',') # Read file 2
 
print(df1.info()) # Info for df1
print(df2.info()) # Info for df2
 
df = df1.append(df2) # Adding df1 and df2 together
 
print(df.info()) # Info for df

### Exercise 8

# Read data files:
# http://www.digitalanalytics.id.au/static/files/spex_4.csv
# http://www.digitalanalytics.id.au/static/files/spex_5.csv
# Explore the files
# Combine them

import pandas as pd
 
df1 = pd.read_csv('http://www.digitalanalytics.id.au/static/files/spex_4.csv',sep=',')
df2 = pd.read_csv('http://www.digitalanalytics.id.au/static/files/spex_5.csv',sep=',')
 
print(df1.info()) # 4 variables, 19342 rows
print(df2.info()) # 6 variables, 19335 rows
 
df = pd.merge(df1, df2, how="left", on=['recommended_artist','recommended_track'])
 
print(df.info()) 
print(df)

### Exercise 9
# Read data file: http://www.digitalanalytics.id.au/static/files/locationdata.csv
# How many observations are in this file?
# Print the unique values in the variable name

import pandas as pd

df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/locationdata.csv', sep=',')
print(df.info())
print(df['name'].unique())

### Exercise 10
# Read data file: http://www.digitalanalytics.id.au/static/files/locationdata.csv
# Create a new variable kfc that contains a value 1 if the substring 'kfc' appears in the all lowercase value of name. Otherwise assign a value 0
# Create a subset that only contains observations with the value 1 for the variable kfc
# How many observations are in that subset?

import pandas as pd

df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/locationdata.csv', sep=',')

def categorisation(name):
	if 'kfc' in name.lower():
		kfc = 1
	else:
		kfc = 0
	return kfc
 
df['kfc'] = df['name'].apply(lambda x: categorisation(x))

subset = df[df['kfc'] == 1]
print(subset.shape)


### Exercise 11
# Read data file: http://www.digitalanalytics.id.au/static/files/locationdata.csv
# Get rid of all observations that have a missing value in the variable phone
# How many observations do have a value for phone?

import pandas as pd

df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/locationdata.csv', sep=',')

df = df.dropna(subset=['phone'])
print(df.info())

### Exercise 12
# Read data file: http://www.digitalanalytics.id.au/static/files/locationdata.csv
# Only keep observations with a value 4000 for postal_code
# How many observations do we keep?

import pandas as pd 

df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/locationdata.csv', sep=',')

postcode = df[df['postal_code'] == 4000]
print(postcode.info())

### Exercise 13
# Read data file: http://www.digitalanalytics.id.au/static/files/locationdata.csv
# Subset the observations with a value Vietnamese restaurant or Thai restaurant in the variable type
# How many observations do we have in the subset?

import pandas as pd 

df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/locationdata.csv', sep=',')

def categorisation(type):
	if type == 'Vietnamese restaurant' or type == 'Thai restaurant':
		keep = 1
	else:
		keep = 0
	return keep
 
df['keep'] = df['type'].apply(lambda x: categorisation(x))
subset = df[df['keep'] == 1]
print(subset.info())
