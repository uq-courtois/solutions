### Exercise 1
 
# Print the result of the multiplication of 88 by 23948

print(88*23948)

# or

z = 88*23948
print(z)

# or (this solution is the most abstract and flexible)

x = 88
y = 23948
z = x*y
print(z)

# Define variable x with value Andy and variable y with value Brown
x = 'Andy'
y = 'Brown'

# Print the concatenation of the values of x and y, with a space in the between
print(x + ' ' + y)

### Exercise 2
 
# Define a list x with the following string values: Jeff, Nadia, Li
x = ['Jeff', 'Nadia', 'Li']

# Insert the string value Erika at the first position of list x
x.insert(0,'Erika')

# Print the first element of list x
print(x[0])

### Exercise 3
 
# Define a list x with the following integer values 5, 8, 4, 1
x = [5, 8, 4, 1]

# Define a variable y that contains the sum of all elements in list x
y = sum(x)

# Print the value of variable y
print(y)

### Exercise 4
 
# Define a list of dictionaries with the information from the table below

# Name Score
# Brad 38
# Lisa 58
# Achmad 78

x = [
{'Name':'Brad','Score':38},
{'Name':'Lisa','Score':58},
{'Name':'Achmad','Score':78},
]

# Change Lisa’s score to 89
x[1]['Score'] = 89

# Print Brad’s score
print(x[0]['Score'])

### Exercise 5
 
# Define a list x with the following integer values 4,6,7,8,4,2
x = [4,6,7,8,4,2]

# Print the value of the smallest integer in x
print(min(x))

# Print the value of the largest integer in x
print(max(x))

# Print the values of the first four values in x
print(x[:4])

### Exercise 6
 
# Define a variable x with the following string value I like turtles
x = 'I like turtles'

# Print the last word in the string value in x
y = x.split(' ')
print(y[-1])
