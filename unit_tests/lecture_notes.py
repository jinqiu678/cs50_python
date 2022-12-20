from calculator_module import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 squared was no 4")

if __name__ == "__main__":
    main()
# Notes
"""
- Writing our own tests to make sure our code does what we want
- use tests to cover all the bases
"""