#Making a copy of a list using a slice of entire original list
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_food)

#Adding a new food to my food list and to my favorite food list
my_foods.append('cannoli')
friends_food.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print(id(my_foods)) #Saved in 4464056192

print("\nMy friend's favorite foods are:")
print(friends_food)
print(id(friends_food)) #Saved in 4464254400


#If on the contrary, we assign a copy of the original list to a new variable
#the two variables will point to the same list in memory

my_foods2 = ['pizza', 'falafel', 'carrot cake']
friends_food2 = my_foods2
print("My favorite foods are:")
print(my_foods2)
print(id(my_foods2)) #Saved in 4492247104
my_foods2.append('cannoli')

print("\nMy friend's favorite foods are:")
print(friends_food2)
print(id(friends_food2)) #Saved in 4492247104
#If we modify the original list, the new variable will also be modified