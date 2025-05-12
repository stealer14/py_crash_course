requested_toppings = []
if requested_toppings: #checks if the list is empty
    for reqeusted_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza")
else:
    print("Are you sure you want a plain pizza?")