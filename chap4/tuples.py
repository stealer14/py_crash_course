#Definining a tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#Tuples are imutable, therefore can't accept any modifications once declared
#dimensions[0] = 100
#print(dimensions)

#Looping through all values in a tuple
for dimension in dimensions:
    print(dimension)
    
#Writing over a tuple (even if a tuple is inmutable)
print("original dimensions")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400,100)
print("\nUpdated dimensions")
for dimension in dimensions:
    print(dimension)
    
