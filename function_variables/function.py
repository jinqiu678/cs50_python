def main():
    hello()
    name = input("What's your name? ")
    hello(name)

# Bringing function definition after the call
# must contain code in main() function, by convention


def hello(to="world"):
    print("Hello", to)


main()

# Notes
"""
- parameters are local scope, cannot be accessed from parent scope
- print is a "side effect", printing to terminal
- return command will return a value explicitely to the program
"""
