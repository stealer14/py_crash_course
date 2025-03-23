for value in range(1,5):
    print(value)
    
#Using rnage to make alist of numbers
numbers = list(range(1,6))
print(numbers)    

#skippiing numbers with range
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#Creating a list of square numbers
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
    
print(squares)

#Replacing intermediate variable for more succint code
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
    
print(squares)
    
#Simple statistics witha  list of numbers
digits = list(range(0,10))
#for num in digits:
#    print(num)

print(min(digits))
print(max(digits))
print(sum(digits))

#List comprehensions
squares2 = [value ** 2 for value in range(1,11)]
print(squares2)

