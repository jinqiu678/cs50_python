from calculator_module import square

def main():
    test_square()

def test_square():
    # if failed return AssertionError
    # use try and except for user friendly
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    
    # default to assertion error
    assert square(3) == 9

if __name__ == "__main__":
    main()

# Notes
"""
- Writing our own tests to make sure our code does what we want
- use tests to cover all the bases
- assert keyword will test if something is true, if not true then error
- Think about the corner cases for tests
- use pytest (one example) program to condense codes and automate testing (e.g. try, except etc.)
- Unit test: test of functions in program, well defined input and outputs
- Good functions either have a "side effect" or return something, not both
- Testable must have return value, not side effects. Test input and return values
- Tests should be nice and simple, not writing tests for or tests
- Package is a python module or modules organized inside a folder
- __init__.py is a indicator to python for a package, create test of folder, run pytest on folder
"""