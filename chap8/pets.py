#Explanation of positional arguments

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} is {pet_name.title()}")

#Mulitple calls to same function and passing different arguments
describe_pet("hamster", "harry")
describe_pet('dog', 'willie')
