# Match, similar to switch in Javascript
name = input("What is your name? ")

match name:
    case "Harry" | "Herminone" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")