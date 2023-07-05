from um import count

def test_character_cases():
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2

def test_word_with_um():
    assert count("yummi") == 0


def test_spaces():
    assert count(" um ") == 1
    assert count("Hello um world") == 1
    assert count("um?") == 1