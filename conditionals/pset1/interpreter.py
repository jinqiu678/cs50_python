mathInputs = input("Expression: ")
x, y, z = mathInputs.split(' ')

match y:
    case '-':
        print(round(int(x) - int(z),1))
    case '+':
        print(round(int(x) + int(z),1))
    case '/':
        print(round(int(x) / int(z),1))
    case '*':
        print(round(int(x) * int(z),1))
    
