players =['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #charles, martina, michael

#Sublist of items 1 through 3
print(players[1:4])

#sublit from beggining to 3
print(players[:4])

#Slic that includes the end of the list
print(players[2:])

#Syntax slice for outputting all of the elements from any point
print(players[-1]) #print last entry
print(players[-3:])

#looping through a slice of a list
print("Here are the first three players on my team::")
for player in players[:3]:
    print(player.title())