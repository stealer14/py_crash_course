import numpy as np
#Using the range function to generate a series of numbers.
for val in range(1,5): #printing values from 1:4, 5 is not inclusive
    print(val)

for val in range(6): #printing values from 1:5, 6 is not inclusive
    print(val)

#Making a list of numbers with range
numbers = list(range(1,6))
print(numbers) #printing the list of numbers

#Using range to make a list of even numbers
even_numbers = list(range(2,11,2)) #2 is inclusive, 11 is not
print(even_numbers) #printing the list of even numbers

#Using range to make a list of odd numbers
odd_numbers = list(range(1,11,2)) #1 is inclusive, 11 is not
print(odd_numbers) #printing the list of odd numbers

#Using range to make a list of squares
squares = []

for value in range (11):
    square = value ** 2
    squares.append(square)

print(squares)

##Calculating simple statistics
minimum = min(squares)
maximum = max(squares)
sumation = sum(squares)

print(minimum)
print(maximum)
print(sumation)
print(np.mean(squares)) #Using numpy to calculate mean

#Using list comprehension to make a list of squares
squares2 = [x**2 for x in range(11)]
print(squares2)