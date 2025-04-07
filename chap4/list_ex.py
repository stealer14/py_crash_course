#Practice problems 4-3 to 4-9
#4-3 Counting from 1 to twenty inclusive
lst1 = list(range(1,21))
print(lst1)

#4-4 LIst from one to 1,000,000
lst2 = list(range(1,1000001))
#print(lst2)

#4-5 Summing a million
min_mill = min(lst2) #minimum value in the million list
print(min_mill)
max_mill = max(lst2) #maximum value in the million list
print(max_mill)
sum_mill = sum(lst2) #sum of the million list
print(sum_mill)

# 4-6 Odd numbers: use third argment of range to make a list of the odd numbers from 1:20. Use for loop to print the numbers
lst3 = list(range(1,20, 2))
#print(lst3)
for num in lst3:
    print(num)

# 4-7 Make a list of multiples of 3 from 3 to 30. use a for loop to print the numbners
lst4 = list(range(3, 31, 3))
print(lst4)
for num in lst4:
    print(num)

# 4-8 Cubes:make a list of the first 10 cubes and use a for loop to print out values
lst5 = list(range(1,11))
for num in lst5:
    cube = num ** 3
    print(cube)
# 4-9 Cube comprehension: use a list comprehension to generate a list of the first 10 cubes
lst6 = [num**3 for num in range(1,11)]
print(lst6)
