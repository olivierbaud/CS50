from jar import Jar
import pytest

def test_init():
    assert Jar().capacity == 12
    assert Jar().size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(20)
    with pytest.raises(ValueError):
        jar.deposit(21)
    jar.deposit(12)
    assert jar.size == 12
    jar.deposit(2)
    assert jar.size == 14


def test_withdraw():
    jar = Jar(50)
    jar.deposit(25)
    with pytest.raises(ValueError):
        jar.withdraw(30)
    jar.withdraw(20)
    assert jar.size == 5