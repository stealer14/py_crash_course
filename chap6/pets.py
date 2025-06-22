# 6-8. Pets: Make several dictionaries, where each dictionary represents a differ-
# ent pet. In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.

pet1 = {'name': 'Rex', 'type': 'dog', 'owner': 'John'}
pet2 = {'name': 'Whiskers', 'type': 'cat', 'owner': 'Jane'}
pet3 = {'name': 'Fluffy', 'type': 'rabbit', 'owner': 'Jill'}

pets = [pet1, pet2, pet3]

for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")