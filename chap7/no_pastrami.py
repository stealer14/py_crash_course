'''
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
'''

#make list of sandiches and store in list
sandwich_orders = ['Tuna melt', 'Pastrami', 'Reuben', 'Pastrami', 'Ham and Cheese', 'Cubano', 'Pastrami']

#make empty list to store orders
finished_sandwich = []

print("\nrecapping order:", sandwich_orders)
print("\nWe're sorry, we're out of pastramit today.")
while 'Pastrami' in sandwich_orders:  #running while loop until sandiwch order list is empty
    sandwich_orders.remove('Pastrami')

print('\n')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwich.append(current_sandwich)

print("\n")
for sandiwhc in finished_sandwich:
    print(f"Your order of {sandiwhc} is made.")
