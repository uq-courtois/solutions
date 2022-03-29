#Define a variable named ‘dataset’ that contains the following information:
#Artist	Track	Plays
#Dire Straits	Sultans of Swing	65
#Pink Floyd	Comfortably Numb	23
#The Smiths	Cemetery Gates	15
#Nick Cave & The Bad Seeds	The Ship Song	36
#Dire Straits	Brothers in Arms	20

dataset = [
  {'Artist':'Dire Straits', 'Track':'Sultans of Swing', 'Plays':65}, 
  {'Artist':'Pink Floyd', 'Track':'Comfortably Numb', 'Plays':23}, 
  {'Artist':'The Smiths', 'Track':'Cemetery Gates', 'Plays':15},
  {'Artist':'Nick Cave & The Bed Seeds', 'Track':'The Ship Song', 'Plays':36},
  {'Artist':'Dire Straits', 'Track':'Brothers in Arms', 'Plays':20}
]

#Print the artist and track (title) of songs with more than 25 plays. Each artist and track combination is printed on a separate line.

for d in dataset:
	if d['Plays'] > 25: # If value of Plays is greater than 25
		print(d['Artist'],d['Track'])

#Loop through the items in dataset. Print all track titles of songs by The Dire Staits. Printing just the titles is ok, each title is printed on a separate line.
#Append all plays to a new list 'plays' during the aforementioned loop. At the end of the script, print the total number of plays. This is the total number of plays of all 5 songs.

plays = [] # Empty list
		
for d in dataset:
	if d['Artist'] == 'Dire Straits': # If value of Artist equals Dire Straits
		print(d['Track'])
	plays.append(d['Plays']) # Add the value of plays to list plays per iteration

print(sum(plays)) # Sum all saved plays values
