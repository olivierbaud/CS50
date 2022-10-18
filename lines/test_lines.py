from lines import check, count
import pytest

def test_no_arg():
    with pytest.raises(SystemExit):
        check(["lines.py"])

def test_extension():
    with pytest.raises(SystemExit):
        check(["lines.py","test.txt"])

def test_manyarg():
    with pytest.raises(SystemExit):
        check(["lines.py","test.py","cat"])

def test_nofile():
    with pytest.raises(SystemExit):
        check(["lines.py","nofile.py"])

test = "#comment\nprint('hello\nname='olivier'\n\n\ncat='black'\n     #test ident\nif True:\n    print(cat)\n"
def test_count():
    file = open("test2.py", "w")
    file.write(test)
    file.close
    assert count("test2.py") == 5
