#Creating and printing elements of a list.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

#using individual items from list
message  = f"My first bicycle was a {bicycles[0].title()}."
print(message)

for item in bicycles:
    print(f"My first bicycle was a {item.title()}.")