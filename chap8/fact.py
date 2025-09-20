#Function to calculate facotiral of a number using recursion
def factorial_r(x):
    #Recursive alternative
    if x == 0 or x == 1:
        return 1
    else:
        fact = x * factorial_r(x - 1)
        return fact

#Function to calculate facotiral of a number using loop
def factorial(n):
    if n <= 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range (1, n + 1):
            result *= i
        return result
        
a = factorial(564)
b = factorial(563)

print(f"percentage !564 over !563 is: {a/b}")
