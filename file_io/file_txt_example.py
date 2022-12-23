name = input("What's your name? ")

# w in write mode will overwrite
# a stands for append
# open will create new file if it doesn't exist, to "persist" in the computer
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

name_list = []
# r - read mode, implicit default
# lines = file.readlines(), rstrip stirng method stripa way new line characters
with open("names.txt", "r") as file:
    # for line in sorted(file)
    for line in file:
        #print("hello,", line.rstrip())
        name_list = [].append(line.rstrip())

# Bring into python and sort, then print out
for name in sorted(name_list):
    print(f"hello, {name}", reverse=True)
    
# Notes
"""
- Transition from memory into saving data and using them persistently
- use _ as pythonic convention for variables that won't be used
- Open keyword is like double clicking on a file to open, "w" will overwrite the file each time
- Use with, more pythonic, automatically close
"""