from calculator_module import square
import pytest

# Break test into different categories. When one function fails, other will run
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

# Test specific error type
def test_str():
    with pytest.raises(TypeError):
        square("cat")
