#Moving items from one list to another

#Start with users that need to be verified
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candance']
confirmed_users = []

#Verify each user until there are no more uncofirmed users.
#Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)


#Display all confirmed users
print("\nThe following users have been confirmed:")

#Iterating over list of confirmed users
for confirmed_user in confirmed_users:
    print(confirmed_user.title())