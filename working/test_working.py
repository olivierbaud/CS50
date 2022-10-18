from working import convert
import pytest

def test_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_night():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_error_min():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_error_sep():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("9: 00AM to 5 :00PM")

