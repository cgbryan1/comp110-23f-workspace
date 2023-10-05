"""Something with lists I guess."""
__author__ = "730657997"

#check whether nums in a list are all equal to input number
def all(listy: list[int], num: int) -> bool:
    idx: int = 0
    while idx < len(listy):
        if listy[idx] != num:
            return False
        idx += 1
    return True

#finds the max in a list of ints.
def max(listy: list[int]) -> int:
    if len(listy) == 0:
        raise ValueError("max() arg is an empty List")
    
    idx: int = 0
    biggest: listy[0]
    #iterate through list and replace biggest with greater values
    while idx < len(listy):
        if biggest > listy[idx]:
            biggest = listy[idx]
        idx += 1
    #return the biggest value
    return biggest

#check if two lists are deeply equal!
def is_equal(list1: list[int], list2: list[2]) -> bool:
    #lists can't be identical if not same length, so check that:
    if len(list1) != len(list2):
        return False
    
    idx: int = 0
    #make sure each item in list is the same, return False if not.
    while idx < len(list1):
        if list1[idx] != list2[idx]:
            return False
        else:
            idx += 1
    #none of the items didn't match, so we return True.
    return True