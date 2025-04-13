#Seeing the world Excercise 3-8
# Think of at lesat five places in whe world you'd like to visit

#Store the location in a list. Make sure the list is not alpahbetical order
places = ['japan', 'peru', 'santorini','athens','new zealand']

# PRint the list in the original order
print("The original list is:", places)

#Use sorted to print your list in alphabetical order without modifying the actual list
print("The sorted list is:", sorted(places))
print("The original list is still:", places)

# USe sorted() to print your list in reverse alphabetical order without modifying the actual list
print("The list in reverse order is:", sorted(places, reverse  =  True))
print("The original list is still:", places)

#Use reverse method() to change the order of your list. Print the list to show that is order has changed.
places.reverse()
print("The permanent list in reverse is:", places)
#Use reverse() to change the order of your list. Print the list to show that its order has changed.
places.reverse()
print("The permanent list in reverse back to original is:", places)

#Use sort() method to change your list so it's stored in alphabetical order. Print the list to show that its order has changed.
places.sort()
print("The list in alphabetical order is:",places)

#Use sort() method to change your list so it's stored in reverse alphabetical order. Print the list to show that its order has changed.
places.sort(reverse = True)
print("The list in reverse alphabetical order is:",places)