#Seing the world: think of at leats fivce places in the workd

#store the lcoations ina  list. make sure is not in alphabetical order
places = ["Australia", "New Zeland", "Japan", "Norway"]

#printing list in original order
print(places)

#print the ist in alphabetical order using sorted()
print(sorted(places))

#Printing original list
print(places)

print("\nPrinting list in reverse order")
places.reverse()
print(places)

print("\nPrinting list in original order once again")
places.reverse()
print(places)

#Using sort to change list (PERMANENTLY)
print("Printing list using sort method")
places.sort()
print(places)

#Using sort to change list (PERMANENTLY) in reverse
print("Printing list using sort method")
places.sort(reverse = True)
print(places)