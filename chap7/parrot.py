#Version now includes prompt to ask if user would like to quit
'''
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
'''

#Setting prompts in separate variables.
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)