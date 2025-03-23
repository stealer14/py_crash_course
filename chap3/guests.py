
#TRy i yourself 2
print("--------------------------")
#Create a guest list of 3-4 people and printing invitation
guests = ["John", "Rick", "Morty"]

print(f"Hello {guests[0]}, you've been invited for dinner.")
print(f"Hello {guests[1]}, you've been invited for dinner.")
print(f"Hello {guests[2]}, you've been invited for dinner.")
len_list = len(guests)
print(f"Length of list is {len_list}")

print("Morty won't be able to make it")
guests[2] = "Mike"

print(f"Hello {guests[0]}, you've been invited for dinner.")
print(f"Hello {guests[1]}, you've been invited for dinner.")
print(f"Hello {guests[2]}, you've been invited for dinner.")

print("A bigger table was found.")
#Addd guest at the beggining of the list
guests.insert(0, "John Wick")

#Addd guest at the middle of the list
guests.insert(2, "Barney Stinson")

#Addd guest at the end of the list
print("--------------------------")
guests.append("Heisenberg")

print(f"Hello {guests[0]}, you've been invited for dinner.")
print(f"Hello {guests[1]}, you've been invited for dinner.")
print(f"Hello {guests[2]}, you've been invited for dinner.")
print(f"Hello {guests[3]}, you've been invited for dinner.")
print(f"Hello {guests[4]}, you've been invited for dinner.")
print(f"Hello {guests[5]}, you've been invited for dinner.")
len_list = len(guests)
print(f"Length of list is {len_list}")

#Shrinking guest list
print("--------------------------")
print("Quick update, there are only two spots available")
a = guests.pop()
print(f"Sorry {a}, I can't invite you.")
len_list = len(guests)
print(f"Length of list is {len_list}")

b = guests.pop()
print(f"Sorry {b}, I can't invite you.")
len_list = len(guests)
print(f"Length of list is {len_list}")

c = guests.pop()
print(f"Sorry {c}, I can't invite you.")
len_list = len(guests)
print(f"Length of list is {len_list}")

d = guests.pop()
print(f"Sorry {d}, I can't invite you.")
len_list = len(guests)
print(f"Length of list is {len_list}")

print(guests) #CHECK remaining invites
print(f"Hello, {guests[0]}, Dinner is still on plan.")
print(f"Hello, {guests[1]}, Dinner is still on plan.")


#deleting last two naems from list, one at a time, or else the list will be out of range
del guests[0]
print(guests)
len_list = len(guests)
print(f"Length of list is {len_list}")

del guests[0]
print(guests) #should be an empty list
len_list = len(guests)
print(f"Length of list is {len_list}")
