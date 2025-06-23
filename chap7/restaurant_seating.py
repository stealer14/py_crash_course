# 7-2 Restaurant Seating

# Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message say-
# ing they’ll have to wait for a table. Otherwise, report that their table is ready.

guest_num = int(input("How many people for reservation? "))

if guest_num > 8:
    print("Apologies, your party will have to wait for a table")
else:
    print("Your party table is ready.")