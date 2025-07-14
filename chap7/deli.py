'''
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop through
the list of sandwich orders and print a message for each order, such as I made
your tuna sandwich. As each sandwich is made, move it to the list of finished
sandwiches. After all the sandwiches have been made, print a message listing
each sandwich that was made.
'''

#make list of sandiches and store in list
sandwich_orders = ['Tuna melt', 'Reuben', 'Ham and Cheese', 'Cubano']

#make empty list to store orders
finished_sandwich = []

while sandwich_orders: #This will keep iterating while the sandiwch order is not empty
    # Extract individual sandiches for order list
    done_meal = sandwich_orders.pop()

    #Print message that order has been made
    print(f"I've made your {done_meal} sandwich.")

    #Store orders in finished list
    finished_sandwich.append(done_meal)

#print message listing each sandiwch made
print("\n---Order complete: itemized list---")
for sandiwch in finished_sandwich:
    print(f"{sandiwch} sandwich was made.")