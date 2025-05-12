cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Check for equality
car = 'audi'
print(car)
print(car == 'bmw') #prints false
print(car == 'audi') #prints true