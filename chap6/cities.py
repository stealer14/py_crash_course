# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the infor-
# mation you have stored about it.

cities = {
    'austin': {
        'country': 'united states',
        'population': 964177,
        'fact': 'austin is the capital of texas',
    },
    'houston': {
        'country': 'united states',
        'population': 2304580,
        'fact': 'houston is the most populous city in texas',
    },
    'dallas': {
        'country': 'united states',
        'population': 1345047,
        'fact': 'dallas is the largest city in texas',
    },
}

for city, city_info in cities.items():
    print(city)
    for key, value in city_info.items():
        print(f"\t{key}: {value}")
    print("\n")