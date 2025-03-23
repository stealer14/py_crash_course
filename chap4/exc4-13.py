foods = ('pizza', 'burguer', 'bread', 'hot dog')

#Using for loop to print each item
for food in foods:
    print(food)
    
#Attempting to replace one of the items, even though tuples are immutable.
'''foods[1] = 'Bakery'
print(foods)
'''
#Updating food menu
foods = ('Taco', 'Pizza', 'Kebab')
for food in foods:
    print(food)