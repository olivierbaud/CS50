from seasons import date_gap
import pytest
from datetime import date, timedelta

tenyears = str(date.today() - 10*timedelta(days=365))

def test_syntax():
    with pytest.raises(SystemExit):
        date_gap("1970, sept 20")
    with pytest.raises(SystemExit):
        date_gap("1970, sept 20")

def test_10years():
    assert date_gap(tenyears) == "Five million, two hundred fifty-six thousand minutes"

def test_date():
    assert date_gap("2020-9-22") == "One million, fifty-one thousand, two hundred minutes"