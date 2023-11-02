"""Testing my summation function."""

from lessons.sum_evens import sum_evens_in_list


def test_empty_sum():
    """Sum_evens_in_list of empty list should be 0."""
    assert sum_evens_in_list([]) == 0


def test_list_length_1():
    """Testing on a list with one element."""
    test_list: list[int] = [2]
    assert sum_evens_in_list(test_list) == 2


def test_list_positives():
    """Testing sum on a list of positive integers."""
    test_list: list[int] = [1, 2, 3, 4]
    assert sum_evens_in_list(test_list) == 6


def test_list_negs_and_pos():
    """Testing sum of negatives and positives."""
    test_list: list[int] = [1, -2, 3, 4]
    assert sum_evens_in_list(test_list) == 2


# tested in terminal by calling python -m pytest lessons/sum_evens_test.py