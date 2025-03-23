print("Hello WOrld")

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

print("---------------------")
#Using format strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

print("---------------------")
#pritingin a ful name
print(f"Hello, my name is {full_name.title()}!")

print("---------------------")
#add a tab to text
print("\tPython")

print("---------------------")
#add new line character
print("Languages: \nPython\C\nJavScript")

print("---------------------")
favorite_language = "Python "
favorite_language = favorite_language.rstrip()