# Load module
import random
import statistics
import sys
# import random as rn
# from random import choice 

# Flip a coin, pseudo-random choice from list
coin = random.choice(["head", "tails"])
print(coin)

# Randomize range of integer between two integer arguments
number = random.randint(1, 10)
print(number)

# shuffle a list of value, randomize order
# This mutates the original list
cards = ["jack", "queen", "king"]
random.shuffle(cards)
print(cards)

# Statistic methods
statistics.mean([1,2,3])

# command-line argument example
# list of all the world inputed during the prompt
# sys.exit prints statement and exits program
if len(sys.argv) < 2:
    sys.exit("Too few Argument")
elif len(sys.argv) > 2:
    sys.exit("too many arguments")
else:
    print("hello, my name is", sys.argv[1])


# Notes
"""
- Functions are tucked away in module files
- Documentation for modules
- import module only will have module prefix in every method
- from random import choice will import choice function in the namespace
- from "module" import * is bad programming practice
- command-line arguments passed as inputs when the program run
- sys.argv[0] is the name of the program, aka name of the file, human input starts at index 1
"""