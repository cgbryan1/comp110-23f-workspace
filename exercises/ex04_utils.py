"""EX04 - practice with lists."""
__author__ = "730657997"


def all(listy: list[int], num: int) -> bool:
    """Check whether nums in a list are all equal to input number."""
    idx: int = 0
    if len(listy) == 0:
        return False
    while idx < len(listy):
        if listy[idx] != num:
            return False
        idx += 1
    return True


def max(input: list[int]) -> int:
    """Finds the max in a list of ints."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    idx: int = 0
    biggest: int = input[idx]
    # iterate through list and replace biggest with greater values
    while idx < len(input):
        if biggest > input[idx]:
            biggest = input[idx]
        idx += 1
    # return the biggest value
    return biggest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """This function checks if two lists are deeply equal."""
    # lists can't be identical if not same length, so check that:
    if len(list1) != len(list2):
        return False
    
    idx: int = 0
    # make sure each item in list is the same, return False if not.
    while idx < len(list1):
        if list1[idx] != list2[idx]:
            return False
        else:
            idx += 1
    # none of the items didn't match, so we return True.
    return True