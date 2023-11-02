"""Summing the elements of a list using different loops."""

author = "__730657997__"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of all list items by using a while loop to iterate through it."""
    sum: float = 0
    idx: int = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Calculates the sum of all elements in vals but uses a for ... in ... loop."""
    sum: float = 0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Calculates the sum of all elements in vals but uses a for ... in range(...) loop."""
    sum: float = 0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum