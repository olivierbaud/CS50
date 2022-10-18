from um import count

def test_spaces():
    assert count("um") == 1
    assert count("um?") == 1

def test_word():
    assert count("Um, thanks for the album.") == 1

def test_sev():
    assert count("Um, thanks, um...") == 2
