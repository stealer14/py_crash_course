#Tuple exercise
# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
food_variety = ('pizza', 'pasta', 'salad', 'soup', 'bread')

# Use a for loop to print each food the restaurant offers.
for food in food_variety:
    print(f"{food.title()} is on the menu.")

# Try to modify one of the items, and make sure that Python rejects the
# change.
food_variety[0] = 'tacos'
print(food_variety) # This will raise a TypeError because tuples are immutable.

# The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.
food_variety  = ('tacos', 'sushi', 'salad', 'sancocho', 'bread')
print('\nUpdated menu:')
for food in food_variety:
    print(f"{food.title()} is on the menu.")