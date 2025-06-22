# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). 
# Maketwo new dictionaries representing different people, and store all 
# three dictionaries in a list called people. Loop through your list of 
# people. As you loop throughthe list, print everything you know about each person.

#Exccercise #1 
# Use a dictionary to store information about a person you know
#Store their
person1 = {'first': 'John', 
           'last':  'Doe',
           'age': 38,
           'city': 'Austin'}

person2 = {'first': 'Jane', 
           'last':  'Doe',
           'age': 36,
           'city': 'Austin'}

person3 = {'first': 'Jill', 
           'last':  'Doe',
           'age': 10,
           'city': 'Austin'}

people_info = [person1, person2, person3]

for person in people_info:
    for entry, ky in person.items():
        print(f"{entry}: {ky}")
    print("\n")