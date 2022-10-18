from fuel import gauge, convert
import pytest

def test_one():
    assert gauge(1) == "E"

def test_99():
    assert gauge(99) == "F"

def test_syntaxe():
    assert gauge(50) == "50%"

def test_convert_round():
    assert convert("1/3") == 33

def test_convert_valueerror():
    with pytest.raises(ValueError):
        convert("4/3")
def test_convert_zerodivision():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

