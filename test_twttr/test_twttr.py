from twttr import shorten

def test_test_upper_lower_case():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("twitter") == "twttr"
    assert shorten("TwitTer") == "TwtTr"


def test_sentence():
    assert shorten("What is your name") =="Wht s yr nm"
    assert shorten("what is your name") =="wht s yr nm"


def test_punctuation():
    assert shorten("?!.,") == "?!.,"


def test_numbers():
    assert shorten("1234") == "1234"
