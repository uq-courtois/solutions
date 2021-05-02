### Tutorial data cleaning

# Exercise 1

import pandas as pd

df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/spotify-output-mani.csv',sep=';')

print(df.info())

df = df.sort_values(by=['tempo'], ascending=False)

print(df[['original_artist','original_track']])

# Exercise 2

import pandas as pd

df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/spotify-output-mani.csv',sep=';')

print(df.duplicated().sum())
print(df[df.duplicated()])
df = df.drop_duplicates()

df.to_csv('spotify-cleanv1.csv',sep=';',index=False) 

# Exercise 3

import pandas as pd

df = pd.read_csv('spotify-cleanv1.csv',sep=';')

print(df.isnull().sum())
isolatemissing = pd.isnull(df['tempo'])
print(df[isolatemissing])
df = df.dropna()

df.to_csv('spotify-cleanv2.csv',sep=';',index=False) 

# Exercise 4

import pandas as pd

df = pd.read_csv('spotify-cleanv1.csv',sep=';')

df['tempocat'] = df['tempo'].apply(lambda x: 1 if x > 100 else 0)

print(df[['tempo','tempocat']])

# Exercise 5

import pandas as pd

df = pd.read_csv('spotify-cleanv2.csv',sep=';')

def tempocatf(x):

	if x <= 90:
		tempocat = 1
	if x > 90 and x <= 120:
		tempocat = 2
	if x > 120:
		tempocat = 3

	return tempocat

df['tempocat'] = df['tempo'].apply(lambda x: tempocatf(x))

print(df[['tempo','tempocat']])
