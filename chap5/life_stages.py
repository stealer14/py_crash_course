# Problem 5-6
# Write an if-elif_else statement that determines a eprson stage of life

age = int(input("Enter your age: "))
stage = None

if age < 2:
    stage = 'baby'
elif age > 2 and age < 4:
    stage = 'todler'
elif age > 4 and age < 13: 
    stage = 'kid'
elif age > 13 and age < 20:
    stage = 'teenager'
elif age > 20 and age < 65:
    stage = 'adult'
elif age > 65:
    stage = 'senior'

print(f"Based on your age, you are a {stage}")