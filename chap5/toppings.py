#Checking inequality
old_requested_topping = 'mushrooms'
if old_requested_topping != 'anchovies':
    print('Hold the anchovies!')

requested_toppings = ['mushrooms', 'extra cheese']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')

print("\nFinished making your pizza!")
