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
# Print the concatenation of the values of x and y, with a space in the between

x = 'Andy'
y = 'Brown'
print(x + ' ' + y)

### Exercise 2
 
# Define a list x with the following string values: Jeff, Nadia, Li
# Insert the string value Erika at the first position of list x
# Print the first element of list x

x = ['Jeff', 'Nadia', 'Li']
x.insert(0,'Erika')
print(x[0])

### Exercise 3
 
# Define a list x with the following integer values 5, 8, 4, 1
# Define a variable y that contains the sum of all elements in list x
# Print the value of variable y

x = [5, 8, 4, 1]
y = sum(x)
print(y)

### Exercise 4
 
# Define a list of dictionaries with the information from the table below
# Change Lisa’s score to 89
# Print Brad’s score
 
# Name Score
# Brad 38
# Lisa 58
# Achmad 78

x = [
{'Name':'Brad','Score':38},
{'Name':'Lisa','Score':58},
{'Name':'Achmad','Score':78},
]

x[1]['Score'] = 89
print(x[0]['Score'])

### Exercise 5
 
# Define a list x with the following integer values 4,6,7,8,4,2
# Print the value of the smallest integer in x
# Print the value of the largest integer in x
# Print the values of the first four values in x

x = [4,6,7,8,4,2]
print(min(x))
print(max(x))
print(x[:4])

### Exercise 6
 
# Define a variable x with the following string value I like turtles
# Print the last word in the string value in x

x = 'I like turtles'
y = x.split(' ')
print(y[-1])
