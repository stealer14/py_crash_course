#Practice example 3-4 Try it yourself
# 3-4. Guest: Write a program that prompts for the user's name and then greets that person.
people_list = ['Nati', 'Matthew', 'Benji']

print(f"Hello {people_list[0].title()}! How you've been?.")
print(f"Hello {people_list[1].title()}! How you've been?.")
print(f"Hello {people_list[2].title()}! How you've been?.")

#3-5 Changing Guest: Start with your program from Exercise 3-4. Write a new program that
cant_attend = people_list[1]
print(f"Sorry {cant_attend.title()} can't make it due to his bed time.")
people_list[1] = 'Amelia'

#Printing a second set of invitation one for each person who is still in the list
print(f"Hello {people_list[0].title()}! How you've been?.")
print(f"Hello {people_list[1].title()}! How you've been?.")
print(f"Hello {people_list[2].title()}! How you've been?.")

#3-6 More Guests: You just found out that you can invite three more people to dinner.
# Add the new guests to the list.
print('---------------------------------------------')
print('The party does need a bigger table')
#using insert() to add new guests
people_list.insert(0, 'Alfredo') #at beggining
people_list.insert(2, 'Michael Scott') #in the middle
people_list.append('Dwight') #using append to add name at the end.
print(people_list)

#Printing a third set of invitation one for each person who is still in the list
for name in people_list:
    print(f"Hello {name.title()}! How you've been?.")

#3-7 Shrinking Guest List: You just found out that your new dinner table won't arrive in time for the dinner, and you have space for only two guests.
print('---------------------------------------------')
print('The party does need a smaller table, as some guests are not coming.')
print("original list", people_list)
#using pop() to remove guests
name = people_list.pop()
print(f"Sorry {name.title()} you are not invited to the dinner.")
print(people_list)

name = people_list.pop()
print(f"Sorry {name.title()} you are not invited to the dinner.")
print(people_list)

name = people_list.pop()
print(f"Sorry {name.title()} you are not invited to the dinner.")
print(people_list)

name = people_list.pop()
print(f"Sorry {name.title()} you are not invited to the dinner.")
print(people_list)
print(people_list[0], "you are still invited to the dinner.")
print(people_list[1], "you are still invited to the dinner.")

#Now we will delete the remaining guests
del people_list[0]
print(people_list)

del people_list[0]
print(people_list)
print("The guest list is empty now.")