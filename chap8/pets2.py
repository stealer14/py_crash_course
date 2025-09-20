# Pests version 2 using keyword arguments
# Defining default values
def describe_pet(pet_name, animal_type = 'dog'): #Using default value
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")



#Using keyword arguments
describe_pet(animal_type='dog', pet_name='willie')
describe_pet(pet_name = 'Harry', animal_type = 'Hamster')
describe_pet(pet_name = "Charles")
 
#Equivalent function alls using positiona, keyword and default arguments
#A dog named Willie
describe_pet('Willie')
describe_pet(pet_name = 'willie')

#A Hamster named Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name = 'harry', animal_type = 'hamster')
describe_pet(animal_type = 'hamster', pet_name = 'harry')