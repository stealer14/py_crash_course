# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”

car_request = input("What kind of rental car you'd like to rent? ")
print(f"Let me see if I can find you a {car_request.title()}.")