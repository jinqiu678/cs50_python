import csv

name = input("What's your name? ")
home = input("WHere's your home? ")

#with open("students.csv", "a") as file:
#    # sole argument, file argument
#    # handle escaping
#    writer = csv.writer(file)
#    writer.writerow([name, home])

### Using Dictionary Instead ####

with open("students.csv", "a") as file:
    # handle escaping
    # order can switch
    writer = csv.DictWriter(file, fieldnames={"name", "home"})
    writer.writerow({"name":name, "home": home})