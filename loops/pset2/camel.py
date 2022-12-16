camel_case = input("camelCase: ")

snake_case = ""
for i in camel_case:
    if i.isupper():
        snake_case = snake_case + "_" + i.lower()
    else:
        snake_case = snake_case + i

print(snake_case)
