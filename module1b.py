### Exercise 1

# Define a list x with values 4, 5, 6, 4, 20
# Add 10 to each number in x and print it

x = [4, 5, 6, 4, 20]

for i in x:
	print(i+10)
 
### Exercise 2

# Define a list x with values 4, 5, 6, 4, 20
# Make a new list y to store new values
# Add 10 to each number in x and add to y
# Print y at the end of the script

x = [4, 5, 6, 4, 20]
y = []

for i in x:
	y.append(i+10)

print(y)

### Exercise 3

# Define a variable x with an interger value of 2
# Wrte a script that multiplies the value of x with itself and prints it as long as the outcome of the multiplication is below 1000

x = 2

while x*x < 1000:
	print(x*x)
	x = x*x

### Exercise 4

# Input the following list of dictionaries into your script
# Name, Age
# Erika, 45
# Leanne, 29
# Lisa, 31
# Annabelle, 30

# Print each dictionary on a separate line

x = [
	{'name':'Erika','age':45},
	{'name':'Leanne','age':29},
	{'name':'Lisa','age':31},
	{'name':'Annabelle','age':30},
	{'name':'Frank','age':50},
	{'name':'Roy','age':70},
]

for d in x:
	print(d)

### Exercise 5

# Dictionary from ex. 4
# Print all the names on a separate line

x = [
	{'name':'Erika','age':45},
	{'name':'Leanne','age':29},
	{'name':'Lisa','age':31},
	{'name':'Annabelle','age':30},
	{'name':'Frank','age':50},
	{'name':'Roy','age':70},
]

for d in x:
	print(d['name'])

### Exercise 6

# Dictionary from ex. 4
# Print all ages that are equal to or larger than 30

x = [
	{'name':'Erika','age':45},
	{'name':'Leanne','age':29},
	{'name':'Lisa','age':31},
	{'name':'Annabelle','age':30},
	{'name':'Frank','age':50},
	{'name':'Roy','age':70},
]

for d in x:
	if d['age'] >= 30:
		print(d['age'])

### Exercise 7

# Dictionary from ex. 4
# Loop through all dictionaries and append all ages to an originally empty list y
# Print that list at the end of the script

x = [
	{'name':'Erika','age':45},
	{'name':'Leanne','age':29},
	{'name':'Lisa','age':31},
	{'name':'Annabelle','age':30},
	{'name':'Frank','age':50},
	{'name':'Roy','age':70},
]

y = []

for d in x:
	y.append(d['age'])

print(y)

### Exercise 8

# Dictionary from ex. 6
# Print the average age of all four persons in the table at the end of the script

x = [
	{'name':'Erika','age':45},
	{'name':'Leanne','age':29},
	{'name':'Lisa','age':31},
	{'name':'Annabelle','age':30},
	{'name':'Frank','age':50},
	{'name':'Roy','age':70},
]

y = []

for d in x:
	y.append(d['age'])

print(sum(y)/len(y))

########## ADDITIONAL - DONE IN THE FIRST TUTORIALS ONLY

# Use the code below to generate a list of 10 random numbers from 0 to 15
# For loop through the list x and only print the numbers larger than 5

import random as rd
x = rd.sample(range(0, 15), 10)
print(x)

for i in x:
	if i > 5:
		print(i)

# Generate a list x of 15 random numbers from 1 to 51
# Loop through x and print each number that is smaller than 5 or larger than 25

import random as rd
x = rd.sample(range(1, 51), 15)
print(x)

for i in x:
	if i < 5 or i > 25:
		print(i)
