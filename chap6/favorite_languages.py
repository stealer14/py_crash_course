#Using diciontaries to store one kind of information about many objects.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

#Extracting the language of specific person
sing_language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {sing_language}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")
#printing keys from dictionary
print("Keys from dictionary:")
for name in favorite_languages.keys(): #.keys can be removed for just looping through keys
    print(name.title())


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

#Looping through a Dictionary's keys in a particular order
print("--------------------------------------------")
print("\nLooping through diciotnary in sorted order")
for name in sorted(favorite_languages):
    print(f"{name.title()}, thank you for taking the poll.")


print("--------------------------------------------")
print("\nLooping through diciotnary values")
for language in favorite_languages.values():
    print(language.title())

print("--------------------------------------------")
print("\nLooping through diciotnary values but sorted")
for language in sorted(favorite_languages.values()):
    print(language.title())

#Using set to avoid any duplicates
print("--------------------------------------------")
print("\nLooping through diciotnary with no repeat values")
for language in set(favorite_languages.values()):
    print(language.title())
