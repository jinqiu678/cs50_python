import csv
# reading csv file, using string methods
# reading file, down the row by default
with open("names.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

# another method, now sorting on names, using dictionary
students = []
with open("names.csv") as file:
    for line in sorted(file):
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

# Python functions are first class functions, can be passed as arguments
# Lambda is anonymous function, nameless function
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")

##### Using CSV Module instead ######
# Gets each row as a list
with open("names.csv") as file:
    # csv.DictReader, returns each row as dictionary, with key as column names
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})