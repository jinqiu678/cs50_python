# convention, captilzie first letter in class
class Student:
    # adding instance variables to objects
    # must include "self", store the variable in the object that's instantiated
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student}.name from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # Student is a constructor
    return Student(name, house)

if __name__ == "__main__":
    main()

# Notes
"""
- functional programming, pass functions around
- return multiple values (unique to python), or return tuple or other data structures with multiple values
- tuple: immutable
- general purpose tool, classes, to create new data types - our own objects
- classes have attribute, can be accessed using ".", can be mutable and inmutable
- ... placeholder for blank functions, classes
- object is the instantiation of a class
- attributes/properties: instance variabes (technical name)
- classes can take arguments
- methods: functions inside classes
- __init__: an instance method, allows the class to take argments as a function
- object is an instance of a class
"""




