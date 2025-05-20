# Problem 5-8 Make a list of give or more users, includng the name 'admin'.
# Imagine you are writing code that will print a greeting to each user oafter they log in to a website.
# Loop through the list and print a greeting to each user

#If the suer name is admin, print a special greeting, such as "Hello admin, would you like to see a status report?"
# Otherwise, print a generic greeting, such as "Hello Eric, thank you for logging in again."

#Declaring list of usernames
#username = ['john', 'morpheus', 'trinity', 'admin', 'neo']
username = []

if username: #check if the list is not empty
    print("The list of users is not empty.")

    #Looping through the list of usernames
    for name in username:
        # Check if user is admin
        if name == 'admin': #print special message
            print(f"Hello {name}, would you like to see a status report?")
        else:
            print(f"Hello {name}, thank you for logging in again.")
else:
    print("We need to find some users!")