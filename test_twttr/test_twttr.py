from twttr import shorten

def test_names():
    names = {
        "John" : "Jhn",
        "david" : "dvd",
        "Olivier" : "lvr",
        "Maxime" : "Mxm",
        "Myriam": "Myrm"}
    for n in names:
        assert shorten(n) == names[n]

def test_cities():
    cities = {
        "Paris" : "Prs",
        "London" : "Lndn",
        "christchurch": "chrstchrch"
    }
    for c in cities:
        assert shorten(c) == cities[c]

def test_numbers():
    assert shorten("CS50") == "CS50"

def test_punct():
    assert shorten("What's your name?") == "Wht's yr nm?"
