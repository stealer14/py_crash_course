#Sorting a list permanently with the .sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse = True) #saves list in place in reverse alphabetical order permanently
print(cars)

print('-----------------------------------------')
print('\n')
#Sorting a list temporarliy with the sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the origina list:')
print(cars)

print('\n')
print('Here is the sorted list:')
print(sorted(cars)) #sorted() function returns a new list

print('\n')
print('Here is the original list sorted in reverse order:')
print(sorted(cars, reverse = True))

print('\n')
print('Here is the original list again:')
print(cars)

print('-----------------------------------------')
print('\n')
#Printing a list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() #reverses the order of the list in place and changes the original list permanently
print(cars)

print('-----------------------------------------')
#Finding the length of a list
print(len(cars)) #len() function returns the number of items in a list