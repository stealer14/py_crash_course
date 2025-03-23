'''#Counting to twenty (print numbers from 1 to 20 inclusive)
for num in range (1, 21):
    print(num)'''
    
#Creating a list containing numbers from 1 to 1,000,000
mill = list()

for num in range(1, 10000001):
    #print(num)
    mill.append(num)
    
#print(min(mill))
#print(max(mill))
#print(sum(mill))

#Using third argument of range, make a list of odd numbers from 1 to 20
#for num in range(1, 20, 2):
#    print(num)

#Make a list of multiples of 3 from 3 to 30. Use a for loop

#First I make a list using conditional to verify all items that are multiple of three

div3 = []
for num in range(1,20):
    if num % 3 == 0:
        div3.append(num)

  
#Using list comprehension
div3 = [num for num in range(1,20) if num % 3 == 0]
print(div3)


#Doing list using steps
for num in range(0,20,3):
    print(num)
    
#Make a list of the cubes from a lsit from 1 to 10
cubes = []
for num in range(1, 11):
    cubes.append(num ** 3)
print(cubes)

#make list of cubes using list comprehension
cubes2 = [num ** 3 for num in range(1, 11)]
print(cubes2)