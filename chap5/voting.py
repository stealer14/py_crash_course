# Simplest kind of condiitional test
age = int(input("How old are you? "))
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote when you turn 18.")