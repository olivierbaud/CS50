import pytest
from numb3rs import validate

def test_range():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False


def test_format():
    assert validate("10.10.10") == False
    assert validate("512.512.512.cat") == False
    assert validate("cat") == False
    assert validate("cat.cat.CAT.cat") == False

def test_first():
    assert validate("192.500.600.700") == False