time = input("What time is it? ")

def main():
    timeInt = convert(time)
    if 7 <= timeInt <= 8:
        print('breakfast time')
    elif 12 <= timeInt <= 13:
        print('lunch time')
    elif 18 <= timeInt <= 19:
        print('dinner time')

def convert(time):
    hours, minutes = time.split(':')
    return int(hours) + int(minutes)/60

if __name__ == "__main__":
    main()