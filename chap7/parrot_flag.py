prompt = "\ntell me someting, and I will repeat back to you:"
prompt  += "\nEnter 'quit to end the program. "

#Setting flag to keep track if program should be running or not
#Flag set outside of loop
active = True

while active:
    message = input(prompt)

    # Escape condition to set flag as false
    if message == 'quit':
        active = False
    
    else:
        print(message)
