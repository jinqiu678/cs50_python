try:
    x = int(input("What's x? "))
except ValueError:
    # replaces default ValueError output
    print("X is not an interger")
else:
    print(f"x is {x}")

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

# Ensure line 12 will be executed from correct input, thus loop with break
def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            # return x = int(input("What's x? "))
            # break
        except ValueError:
        # replaces default ValueError outputs
            # print("X is not an interger")
            pass # won't show any statement when error occurs
        else:
            break
            # return x
    return x

print(f"x is {x}")

# Notes
"""
- Exceptions, not a good thing in programmning, does not mean exceptional
- SytaxError: something is syntactically wrong with the code
- ValueError: illegal datastructure usage
- NameError: variable error, tends to do with my code
- String interpolation interprets the string literal with placeholders
- "try" to do something "except" when something goes wrong "else" do this
- "pass" say nothing when error occurs
- Can catch every error, but may cause unintended error, not good programming practice
"""