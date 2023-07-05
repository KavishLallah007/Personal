from plates import is_valid

# length between 2 and 6 inclusive
def test_length():
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

# Not start with numbers
def test_start_with_two_letters():
    assert is_valid("AB") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("12") == False

# First number must not be zero
def test_first_num_not_zero():
    assert is_valid("AB50") == True
    assert is_valid("AB05") == False

# No numbers between letters
def test_num_in_middle():
    assert is_valid("ABC50") == True
    assert is_valid("AB50C") == False

# No punctuation periods or spaces are allowed
def test_no_punctuations():
    assert is_valid("AA.55") == False
    assert is_valid("AA50!") == False
    assert is_valid("AA 50") == False