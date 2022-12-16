for i in range(3):
    print("meow")

for _ in range(3):
    print("meow")

# Operator on string, using backslash
# removing last blank line changing default end argument
print("meow\n" * 3, end="")

# Break loop if n is positive, ensuring input is not negative
def get_number():
    while True:
        n = int(input("What is n "))
        if n > 0:
            break
    return n

# Create meow function
def main():
    number = get_number()
    meow(number)

def meow(n):
    for _ in range(n):
        print("meow")

main()

# List examples and indexing
students = ['Herald', 'Harry', 'Ron']
print(students[0])

for student in students:
    print(student)

# Way to get index in loop
for index in range(len(students)):
    print(index)
    print(students[index])
    print(i + index, students[index])

# dict: dictionary, keys and value
# keys have to be unique
students = {
    "Harmone": "Gryffindor", 
    "Ron": "Gryffindor",
    "Draco": "Slyterin",
    "Harry": "Gryffindor"
}

for student in students:
    print(student, students[student], sep=", ")
    
# Compose list of dictionaries, nested data structure
students = [
    {"name": "Hermone", "house":" Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house":" Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house":" Gryffindor", "patronus": "Jack Russel"},
    {"name": "Draco", "house":" Slytherine", "patronus": None}
]

for student in students:
    print(student['name'], student['house'], student['patronus'])

# Notes
"""
- use _ as a variable that won't be used later, pythonic way
- default while to True, a common paradigm in python
- list is a datatype in python, similar to array in javascript
- like javascript, python index starts at 0
"""