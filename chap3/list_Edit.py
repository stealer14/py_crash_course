motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  

#print first element
print(motorcycles[0])

#Replacing first element
motorcycles[0] = 'ducati'
print(motorcycles)

#Add element to the end of a a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati)')
print(motorcycles)

#Appending items to an empty list
motorcycles_new = []
motorcycles_new.append('honda')
motorcycles_new.append('yamaha')
motorcycles_new.append('suzuki')
print(motorcycles_new)

#Inserting element to a list with .insert() method
print("+-----------------")
print("Using insert() method")
motor = ['honda', 'yamaha', 'suzuki']
motor.insert(0, 'ducati')
print(motor)

#Removing elements from a list
print("+-----------------")
motor = ['honda', 'yamaha', 'suzuki']
print(motor)

#deleting specific element form list, in this case, the first element
del motor[0]
print(motor)

#Deleting specific element, in this case the first element
motor = ['honda', 'yamaha', 'suzuki']
print(motor)
del motor[1]
print(motor)

#Removing elements from a list using Pop() method
print("+-----------------")
print("Using pop() method")
motor = ['honda', 'yamaha', 'suzuki']
print(motor)
popped_motor = motor.pop()
print(motor, "original list minus last item")
print(popped_motor, "popped item")

#poping any element from a list by specifying the item
print("+-----------------")
motor = ['honda', 'yamaha', 'suzuki']
print(motor)
first_owned = motor.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

#Using remove() method to remove an item from a list
print("+-----------------")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive= 'ducati'
motorcycles.remove(too_expensive)
print(f"\nA {too_expensive.title()} is too expensive for me.")
