"""Test my zip function!"""
__author__ = "730657997"

from lessons.zip import zip


def test_empty_list():
    """Checks to see if fxn works with empty lists (edge case)."""
    my_strings: list[str] = []
    my_ints: list[int] = []
    
    assert zip(my_strings, my_ints) == {}


def test_good_list():
    """Checks to see if a fxn works with normal lists (use case)."""
    my_strings: list[str] = ["Hello", "Howdy", "Hey", "Hi"]
    my_ints: list[int] = [5, 5, 3, 2]
    
    assert zip(my_strings, my_ints) == {'Hello': 5, 'Howdy': 5, 'Hey': 3, 'Hi': 2}


def test_mismatch_list():
    """Checks to see if function works with mismatched lists (use case)."""
    my_strings: list[str] = ["Hello", "Howdy", "Hey", "Hi"]
    my_ints: list[int] = [1, 2]
    
    assert zip(my_strings, my_ints) == {}

# tested in terminal by calling python -m pytest lessons/zip_test.py