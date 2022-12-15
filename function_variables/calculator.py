# Integer
x = int(input("What's X? "))
y = int(input("What's y? "))
z = x + y
print(z)

# Float
x = float(input("What's X? "))
y = float(input("What's y? "))
z = x + y
print(z)

# Round, in documentation: round(number[, ndigits]),
# one number and square brackets are optional
print(round(z))

# f string to format
toFormat = float(input("What number do you want to format? "))
print(f"{toFormat:,}")
print(f"{toFormat:.2f}")

# Notes
"""
- +, -, *, / are operators in python
- % is modulo operation
- python, enter into python shell in terminal
- user input will also be text, and rendered as string
- use int() function to change datatype into integer
- functions can be nested, return of a function between argument to next function
"""
