# Write a loop that prompts the user to enter a series 
# of pizza toppings until they enter a 'quit' value.
# print a message that you'll add that topping to the pizza

activity = True
while activity:

    ingredient = input("Enter an ingredient: ")

    if ingredient == 'quit':
        activity = False
    else:
        print(f"{ingredient.title()} added to your pizza.")