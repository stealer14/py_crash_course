#Checking inequality
old_requested_topping = 'mushrooms'
if old_requested_topping != 'anchovies':
    print('Hold the anchovies!')

requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
'''
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
'''

for topping in requested_toppings:
    print(f"Adding {topping}")
    if topping == 'green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print(f"Adding {topping}")
print("\nFinished making your pizza!")
