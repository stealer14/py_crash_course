#Excercise 8-3
'''
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print a
sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.

No default arguments in this function
'''

def make_shirt(size, message):
    """ A function that creates a summarize tshirt order listing message 
    and tshirt size.
    Inputs:
    size (char) = S, M, L, XL, XXL
    message (str): message to be displayed 
    """

    print(f"Order summary: Tshirt size is {size.capitalize()}, and message is: {message.title()}.")

make_shirt('l', 'Live Long and Prosper')