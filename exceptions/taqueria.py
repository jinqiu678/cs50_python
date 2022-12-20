menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

item_total = 0
while True:
    try:
        item = input("Item: ").title()
        item_total = item_total + menu[item]
        for i in menu.keys():
            if item == i:
                print("Total", f"${item_total:.2f}")
            else:
                continue
    except EOFError:
        print('\n')
        break
    except KeyError:
        pass
        


