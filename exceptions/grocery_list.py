item_dict = {}
while True:
    try:
        item = input()
        if item in item_dict:
            item_dict[item] += 1
        else:
            item_dict[item] = 1
    except EOFError:
        print('\n') 
        break

for i in item_dict:
    print(item_dict[i], i.upper())

