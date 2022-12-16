def main():
    prompt = input("What i your emoji? ")
    emoji = convert(prompt)
    print(emoji)

def convert(str):
    converted = str.replace(':)', ' 🙂')
    converted = converted.replace(':(', ' 🙁')
    return converted

main()