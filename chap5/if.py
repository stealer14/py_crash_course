'''cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
#Checking multiple conditions at a time
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)


#CHecking that a value is contained within a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

#using not in to indicate that value is not contained within collection data
banned_users = ['andrew', 'carolina' , 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
    
#Try yourself 5-1 Conditional Test
car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

print("\nIs car == 'audi'. I predict False")
print(car == 'audi')

print("\nIs car == 'mazda' in the car list. I predict False")
print('mazda' in cars)
'''
#Asking age for voting
'''
print("--------Age Checking----------")
age = int(input("What is your age: "))
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("You are too young to vote.")
'''

#Asking age for admission ticket
#age = 12
age = int(input("Enter age: "))
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40")
'''    
#Making above code more succint. Makes easier for maintaining and apply changes.
age = 19
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your age is {age} and the admission cost is ${price}.")

lst = [1,2,3,4,5]
for item in lst:
    x = item + 10
    print(f"The original number is {item} and the new number is {x}.") #prints original number and new number (x)'''