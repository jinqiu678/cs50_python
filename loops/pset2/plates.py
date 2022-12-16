def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[len(s) - 1].isalnum():
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    for i in s:
        if not i.isalnum():
            return False

    # Check first number is not 0, without using regex
    for i in s:
        if i.isnumeric():
            if int(i) == 0:
                return False
            break

    return True


    



main()