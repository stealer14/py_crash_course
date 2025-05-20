# 5-10 Checking username:
# Do the follogin to create a program that simulates how websites ensure that everyone has a unique username.
# make a list of five or more usernames called current_users.
current_users = ['admin', 'user1', 'user2', 'user3', 'user4']

# make another list of five usernames called new_users.
new_users = ['admin', 'user5', 'user6', 'user7', 'user8']
# loop through the new_users list to see if each new username has already been used.

for user in current_users:
    if user.lower() in new_users:
        print(f"{user} is already taken, please choose a different username.")
    else:
        print(f"{user} is available.")
