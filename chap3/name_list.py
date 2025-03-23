'''
friend_names = ["Marcos", "Jorge", "Francisco", "Frank"]
print(f"My first friend from school is {friend_names[0].title()}")
print(f"My second friend from school is {friend_names[1].title()}")
print(f"My third friend from school is {friend_names[2].title()}")
print(f"My fourth friend from school is {friend_names[3].title()}")

#Changing elements of lists
motorcycles = ['honda', 'yamaha','suzuki']
print(motorcycles)

#replacing second element
motorcycles[1] = 'ducati'
print(motorcycles)

#appending to end of list
motorcycles1 = ['honda', 'yamaha','suzuki']
motorcycles1.append('ducati')
print(motorcycles1)

#Using insert into to enter an element into a specific slot in alist
motorcycles2 = ['honda', 'yamaha','suzuki']
motorcycles2.insert(0, 'ducati')
print(motorcycles2)

#Removing item from list using del
del motorcycles2[0]
print(motorcycles2)

#Using pop method, returns and remove last item from a list
popped_motorycle = motorcycles2.pop()
print(popped_motorycle)

#Using pop to remove any item from the list by specifying index
popped_motorycle2 = motorcycles2.pop(1)
print(popped_motorycle2)
print(motorcycles2)
'''

'''
current_motorycles = ['honda', 'yamaha','suzuki', 'ducati']
too_expensive = 'ducati'
current_motorycles.remove(too_expensive)
print(current_motorycles)
print(f"\nA {too_expensive.title()} is too expensive for me")
'''
