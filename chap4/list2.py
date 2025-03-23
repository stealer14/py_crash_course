#Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[:4]) #without start and end index indication
print(players)
print(players[-3:])

#Looping thoruhg a slice
print("Here are the first three players on my team.")
for player in players[:3]:
    print(player.title())
    
#Copying a list
my_food = ['pizza', 'falafel', 'carrot cake']
friend_food = my_food[:] #making a copy of oriignal list
print("My favorite foods are:")
print(my_food)

print("\nMy friend's favourite foods are:")
print(friend_food)

#addign new food 
print(my_food == friend_food)
my_food.append("canoli")
friend_food.append("ice cream")

print("My favorite foods are", my_food)
print("My friend's favorite foods are: ", friend_food)