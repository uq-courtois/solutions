### URLS

#http://www.digitalanalytics.id.au/static/files/billboard1.csv
#http://www.digitalanalytics.id.au/static/files/billboard2.csv

#http://www.digitalanalytics.id.au/static/files/billboard_additional.csv

### Get unique values in variable

print(df['variable'].unique())
print(len(df['variable'].unique()))

### Exercise 7

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
		popularity = 'low'
	if x >= 33 and x < 66:
		popularity = 'medium'
	if x >= 66:
		popularity = 'high'

	return popularity

df['popularitycat'] = df['popularity'].apply(lambda x: popularityf(x))
