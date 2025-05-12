# 5-3 
# Imagine an alien was just shot down in a game. create a variable 
# called alien_color and assign a velu of green, yellow or red
alien_color = input('Enter color of the alien: ')
print(f"Alien color is {alien_color}")

if alien_color == 'green':
    print("You just earned 5 points")
elif alien_color == 'yellow':
    print("You just lost 5 points")
elif alien_color == 'red':
    print("You just lost the game")
else:
    print("I don't know what to do")


#Create a script for web crawling a webpage and check if the color of the alien is green, yellow or red
