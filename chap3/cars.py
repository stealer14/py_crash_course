
#Sorting a list permanently with the sort() method.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#Reversing order of list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#using surted to temporarliy sort a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("here's the original list")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere's the original list again: ")
print(cars)

cars.reverse() #reverse method acts in place, and if trying to store in a variable, it will return None
print(cars)

#finding length of a list
print(len(cars))