from twttr import shorten
import pytest

def test_lowercase():
    assert shorten('my name is jin') == 'my nm s jn'

def test_uppercase():
    assert shorten('MY NAME IS JIN') == 'MY NM S JN'

def test_non_string_inputs():
    with pytest.raises(TypeError):
        shorten(5)
        shorten(True)
        shorten({})
        shorten([])
        shorten(5.123)