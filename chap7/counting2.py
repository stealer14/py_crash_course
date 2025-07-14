#Using continue in a loop
# printing numbers from 1 to 10 but only if they're even.

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


#Avoiding infinite loops
'''
x = 1
while x <= 5:
    print(x) # without any increments, x is always 1, and less than 5'''