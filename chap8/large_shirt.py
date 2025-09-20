#Excercise 8-4: Large Shirts

'''
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
'''

def make_shirt(size = 'L', message = 'I Love Python'):
     """ A function that creates a summarize tshirt order listing message 
    and tshirt size.
    Inputs:
    size (char) = S, M, L, XL, XXL. Default value = L
    message (str): message to be displayed. Default is I love Python
    """
     print(f"Tshirt size is {size.capitalize()} and message is \"{message.title()}\".")

make_shirt() #default value of Large shirt with default message
make_shirt('m') #changed tshirt to medium
make_shirt('s', 'Life is a highway') #
make_shirt(message = "Beef is what's for dinner", size = 'XXL', ) # specifying keyword arguments in no respective order