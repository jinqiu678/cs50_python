def main():
    fraction = input("Fraction: ")
    x, y = fraction.split('/')
    try:
        ratio = int(x) / int(y)
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        print(fuelConversion(ratio))


def fuelConversion(input):
    if input <= .01:
        return "E"
    elif input >= .99:
        return "F"
    else:
        return f"{round(input * 100)}%"

main()