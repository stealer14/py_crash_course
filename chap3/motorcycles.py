#Modifying, adding and removing elements of a list.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)

#adding element 
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

empty_list = []
empty_list.append('honda')
empty_list.append('yamaha')
empty_list.append('suzuki')
print(empty_list)

#Inserting item into list
motorcycles.insert(0, 'ducati')
print(motorcycles)