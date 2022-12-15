# Ask user for their name
name = input("what is your name? ")

# Say hello to user using fstring
print(f'hello, {name}')

# Say hello to user multiple arguments in print, space is default seperator
print('hello,', name)

# Say hello to user using string concatenation
print('hello, ' + name)

# Rewriting end parameter
print('hello', name, sep='???')

# Removing whitespace from str, using methods from str datatype
nameCleaned = name.strip().title()
print('hello, ' + nameCleaned)

# Str split method, splitting into multiple substrings, return sequence of variables
first, last = nameCleaned.split(" ")
print(f"hello", first)
print(f"hello", last)

# Notes
"""
- docs.python.org, official documentations
- print(*objects, sep=' ', end='/n', file=sys.stdout, flush=False)
- *objects: any number of objects
- sep=' ': default is space, seperating each argument
- end='\n`: creates new line after passing in all the arguments
- parameters: what you can pass to function
- arguments: what is actually being passed
- Consistent between double and single quote
- \ backslash is a escape character
- python can assign multiple variables in one line
"""