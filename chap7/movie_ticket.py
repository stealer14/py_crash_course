'''
7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
'''

while True:
    answer = input("Enter your age: ")

    if answer == 'quit':
        print("Bye Bye")
        break

    else:
        #Convert input to integer
        age = int(answer)

        if age < 3:
            print("Entrance is free")

        elif age >=3 and age <= 12:
            print("Ticket cost $10.00")

        else:
            print("Ticket cost $15.00") 