import sys
import csv

def main():
    if len(sys.argv) != 2:
        sys.exit("Incorrect amount of command-line arguments")
    elif not sys.argv[1].endswith(".csv" ) and sys.argv[2].endswith(".csv" ):
        sys.exit("Incorrect file format")
    
    file_name = sys.argv[1]

    data = read_file(file_name)
    write_new_file(data)

def read_file(file_name):
    file_lines = []
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            first_name, last_name = row["name"].split(", ")
            house = row["house"]
            file_lines.append(
                {"first_name": first_name,
                "last_name": last_name,
                "house": house}
            )
    return file_lines
    
def write_new_file(data):
    with open("after.csv", "w+") as file:
        writer = csv.DictWriter(file, fieldnames=["first_name",
        "last_name", "house"])
        writer.writeheader()

        for dict in data:
            writer.writerow(dict)

if __name__ == "__main__":
    main()