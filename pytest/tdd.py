import pytest
from my_module import is_password_valid, count_valid_passwords_from_file

def test_is_password_valid():
    assert is_password_valid("1-3 a", "abcde") == True
    assert is_password_valid("1-3 b", "cdefg") == False
    assert is_password_valid("2-9 c", "ccccccccc") == True

def test_txt_file():
    assert count_valid_passwords_from_file("data.txt") == 454




#if __name__ == "__main__":
