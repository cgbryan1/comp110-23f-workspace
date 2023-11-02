"""Combining two lists into a dictionary."""
__author__ = "730657997"


def zip(keys: list[str], vals: list[int]) -> dict[str, int]:
    """Each str in keys shoud correspond w a num in vals."""
    # tried this with {} and it didn't work either?
    my_dict: dict[str, int] = {}

    if (len(keys) != len(vals) or len(keys) == 0 or len(vals) == 0):
        return my_dict
    
    for idx in range(0, len(keys)):
        my_dict[keys[idx]] = vals[idx]
    
    return my_dict


print(zip(["Happy", "Tuesday"], [1, 2]))