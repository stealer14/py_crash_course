#If elif else statements

'''
The if-elif-else chain is powerful, but it’s only appropriate to use when you
just need one test to pass. As soon as Python finds one test that passes, it
skips the rest of the tests. This behavior is beneficial, because it’s efficient
and allows you to test for one specific condition.
'''
age:int = 12

if age < 4:
    print("Your admision cost ist $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admision cost is $40")

#More conscise if stamenet
age = 45

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")