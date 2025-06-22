'''
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When
you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.
'''

#Think of five progrmming words you've learned
glossary = {
    'variable': 'A named storage location for a value.',
    'function': 'A block of code that performs a specific task.',
    'loop': 'A control structure that repeats a set of instructions until a certain condition is met.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'tuple': 'An immutable ordered collection of items.'
}
#printing ehac word invidually with its meaning
#print(glossary['variable'])
#print(glossary['function'])

#using a for loop
for word, definition in glossary.items():
    print(f"{word.title()}: {definition}")

