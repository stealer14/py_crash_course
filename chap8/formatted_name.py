#Returning a simple value
def get_formatted_name(first_name, last_name):
    """Return  a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#Expanding above function to add optional argument for middle name. Optional value goes at the end
def get_formatted_full_name(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formatted"""
    if middle_name: #if a value is proivded for middle name, return full name
        full_name = f"{first_name} {middle_name} {last_name}"

    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

movie_star = get_formatted_full_name('robert', 'downey', 'jr')
print(movie_star)

actor = get_formatted_full_name('jay', 'barouche')
print(actor)

historic_figure = get_formatted_full_name('john', 'hooker', 'lee')
print(historic_figure)