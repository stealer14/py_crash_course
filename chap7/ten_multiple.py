# 7-3 Multiples of ten

# ask the user for a number and report wheter the number is
# multiple of ten or not.

num = input("Please enter a number: ")
num = int(num)

if num % 10 == 0:
    print(f"Number {num} is multiple of 10.")
else:
    print(f"{num} is not multiple of 10.")

