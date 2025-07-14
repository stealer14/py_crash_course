'''
7-10. Dream Vacation: Write a program that polls users about their dream vaca-
tion. Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll.
'''

#Declare empty dictionary to store responses
responses = {}

#Set flag to indicate that polling is active
poll_active = True

#Set while loop to capture respsonses
while poll_active:
    #propt for the person's name and response
    name = input("\nWhat is your name: ?") #key
    response = input("Tell me your dream vacation: ") #value

    #Store response in dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    #set input requirement to change poll active flag to false and end the loop
    repeat = input("Would you like to let another person respond (yes/no): ")
    if repeat == 'no':
        poll_active = False

#Now that the loop and polling is completed, show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name}'s dream vacation is: {response}.")