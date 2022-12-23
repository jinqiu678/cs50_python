import sys

def main():
    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]

    if not file_name.endswith(".py"):
        sys.exit("Not a Python File")  
    
    count_file_lines(file_name)


def count_file_lines(file_name):
    file_lines = []
    try:
        with open(file_name) as file:
            for line in file:
                clean_line = line.strip()
                if clean_line.startswith("#") or clean_line == '':
                    continue
                else:
                    file_lines.append(clean_line)
    except FileNotFoundError:
        print("File does not exists")
    else:
        print(len(file_lines))

if __name__ == "__main__":
    main()
            