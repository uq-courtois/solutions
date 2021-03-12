### TUTORIAL 1B - Conditionals and Loops

# Exercise 1

import random as rd
x = rd.sample(range(0, 15), 10)
print(x)

for i in x:
	if i > 5:
		print(i)

# Exercise 2

import random as rd
x = rd.sample(range(1, 51), 15)
print(x)

for i in x:
	if i < 5 or i > 25:
		print(i)

# Exercise 3

x = [4,5,6,4,20]
y = []

for i in x:
	y.append(i+10)

print(y)

# Exercise 4

x = 2

while x*x < 1000000:
	x = x*x
	print(x)

# Exercise 5

x = [
	{'name':'Erika','age':45},
	{'name':'Leanne','age':29},
	{'name':'Lisa','age':31},
	{'name':'Annabelle','age':30},
]

for i in x:
	if 'an' in i['name'].lower():
		print(i['name'])

# Exercise 6

x = [
	{'name':'Erika','age':45},
	{'name':'Leanne','age':29},
	{'name':'Lisa','age':31},
	{'name':'Annabelle','age':30},
]

y = []

for i in x:
	y.append(i['age'])

print(sum(y)/len(y))

# Exercise 7

x = ['Lisa','Lisa','Lisa','Erik']

while 'Lisa' in x:
	x.remove('Lisa')

print(x)

# Exercise 8

x = [4,7,6,5,20]

for i in x:
	y = i/2
	if y.is_integer():
		print(i,'is an even number')
	else:
		print(i,'is an odd number')
