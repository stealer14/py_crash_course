#Favorite language printing with all whitespaces
favorite_language = '  Python  '
print(favorite_language)

#Printing string withohth whitespace on the right trailing
favorite_language = favorite_language.rstrip()
print(favorite_language)

#Printing string withohth whitespace on the left leading
favorite_language = favorite_language.lstrip()
print(favorite_language)

url = 'https://nostarch.com'
new_link = url.removeprefix('https://')
print(new_link)


#2-3 PErsonal Mesage
name = "Eric"
var1 = f"Hello {name}, would you liek to learn some Pythonn today?"
print(var1)
print(name.lower())
print(name.upper())
print(name.title())

#Printing quotes
famous_person = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
print(famous_person)

filename = 'python_notes.text'
print(filename.removesuffix('.text'))
