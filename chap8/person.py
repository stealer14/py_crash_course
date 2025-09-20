#Returning a dictionary

def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

#Extending function to include age
def build_full_person(first_name, last_name, age = None):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_full_person('jimi', 'hendrix', age=28)
print(musician)

doctor = build_full_person('john', 'kevorkian')
print(doctor)
