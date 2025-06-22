rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China',
    'Mississippi': 'United States',
    'Danube': 'Europe',
}

for river, country in rivers.items():
    print(f"river name: {river}")
    print(f"country name: {country}")
    print(f"The {river.title()} runs through {country.title()}.")
    print("\n")