# 6-2 Favorite Number:
# use a dictionary to store people's favorite numbers.
# think of five names and use them as keys in your dictionary.
# Assign a favorite number for each person and store as a value in dictionary
# print each person's name and their favorite number.

import random

fav_num = {
    'john': random.randint(1, 100),
    'jane': random.randint(1, 100),
    'jim': random.randint(1, 100),
    'jill': random.randint(1, 100),
    'joe': random.randint(1, 100),
}

for name, num in fav_num.items():
    print(f"{name.title()}'s favorite number is {num}")