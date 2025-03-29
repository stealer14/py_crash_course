#Try it yourself problems 
friends = ['Matthew', 'Marcos', 'Jorge', 'Alfredo', 'Francisco']
print(f'Hello {friends[0]}, long time no see.')
print(f'Hello {friends[1]}, long time no see.')
print(f'Hello {friends[2]}, long time no see.')
print(f'Hello {friends[3]}, long time no see.')
print(f'Hello {friends[4]}, long time no see.')
#3-1 store and print individual name of friend list.
for _ in friends:
    print(_)

#3-2 print a personalized message (text remaining the same) but addressed o each name

for name in friends:
    print(f'Hello {name}, long time no see.')

#3-3 print your own list of favorite mode of transportation now using a while loop
transpo = ['Lamborghini', 'Ducati', 'Range Rover']

i = 0
while i < len(transpo):
    print(f"I would love to won a {transpo[i]}.")
    i += 1

