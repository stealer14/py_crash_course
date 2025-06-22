#Declaring dictionary with alien features
alien_0 = {'color': 'green', 'points': 5}

#Decllaring empty dict
new_alien = {}
new_alien['color'] = 'dark green'
new_alien['points'] = 5
print(new_alien)

#Single dictionary would look like:
alien_single = {"color": "green"}

print(alien_0['color'])
print(alien_0['points'])

# Accessing values in a Dictionary
# use name of dictionary and [key] to access
print(alien_0['color'])

#Adding coordinates to alien
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Modifying values in a dictionary
print(f"The alien is {alien_0['color']}.")

#replacing color
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

print("----------------------------")
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

#Move the alien to the right:
# Determine how far to mov the alien based on current speed
alien_0['speed'] = 'Fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien
    x_increment = 3

#The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

#deleting item
alien_0 = {'color': 'green', 'points': 5}
del alien_0['color']
print(alien_0)