# 4-8 cubes: make a list of the first 10 cubes from 1 to 10

cubes = list(range(1, 11))
for num in cubes:
    print(num ** 3)

# 4-9 cube comprehension: use alist comprehension t geenrate
# a list of the first 10 cubes
cubes2 = [val ** 3 for val in range(1, 11)]
print(cubes2)