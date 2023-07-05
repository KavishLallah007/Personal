from bank import value

def test_hello():
    assert value("Hello") == 0

def test_start_h():
    assert value("Hey") == 20
    assert value("How are you doing?") == 20

def test_not_start_h():
    assert value("What's up") == 100
    assert value("Good morning") == 100