from python import is_password_valid, count_valid_passwords_from_file

def test_is_password_valid_false():
    assert is_password_valid("1-3 b", "cdefg") is False

def test_is_password_valid():
    assert is_password_valid("1-3 a", "abcde") is True
    assert is_password_valid("2-9 c", "ccccccccc") is True

def test_txt_file():
    assert count_valid_passwords_from_file("data.txt") == 454

# To run the tests, enter `pytest` in your terminal.