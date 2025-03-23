#hapter 4 Try it yourself

#THink of three kinds of pizza, stor ehtese names in a list, and use a for loop to print hte name of each pizza
pizza_fav = ['peperoni', 'stravaganza', 'ham & cheese', 'veggie']
for pizza in pizza_fav:
    print(pizza)
    
print("--------")
    
#print a sentence using the name of the pizza
for pizza in pizza_fav:
    print(f"I really love having {pizza.title()} pizza.")
print("\nI mean I don't know if you can tell")
print("...but...")
print("I really like pizza.")