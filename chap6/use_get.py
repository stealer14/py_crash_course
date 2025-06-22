alien_0 = {'color': 'green', 'speed': 'slow'}

#Attempting to print a value from a key that does not exist
#print(alien_0['points']) #This does not work

point_value = alien_0.get('points', "No point value assigned")
print(point_value)