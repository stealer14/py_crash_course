#Greet user program part 2
#MOdifying function to accept user name

def greet_user(name): #name is the parameter listed in the functio definition
    """Display a simple greeting to specific user"""
    print(f"Helllo, {name.title()}!")

greet_user("jesse") #function call with argument (actual value that is passed to the function)
greet_user('sarah')
greet_user('matthew')