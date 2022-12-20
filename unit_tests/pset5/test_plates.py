from plates import is_valid
import pytest

def test_length():
    assert is_valid('KFGMKFGKMKFG') == False
    assert is_valid('1') == False

def test_end_with_number():
    assert is_valid("hidf24") == True
    assert is_valid("gg32") == True

def test_start_with_number():
    assert is_valid('12gg') == False
    assert is_valid('23gass') == False

def test_punctuations():
    assert is_valid('pla!.!s') == False
    assert is_valid('??..!') == False