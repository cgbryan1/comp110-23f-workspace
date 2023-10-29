"""This is where I'll implement my function skeletons and implementations below."""

__author__ = "730657997"


def invert(original: dict[str, str]) -> dict[str,str]:
    """Inverting a dictionary."""
    inverted: dict[str, int] = {}

    for key in original:
        if original[key] in inverted:
           raise KeyError("Can't assign two values to the same key!")
        else:
           inverted[original[key]] = key

    return inverted


def favorite_color(original: dict[str, str]) -> str:
    """This function takes a dictionary of favorite colors and returns the most common favorite."""
    # create a dict with each color as a key, and then add to the value for its frequency.

    color_frequency: dict[str, int] = {}

    for key in original:
        color: str = original[key]

        if color in color_frequency:
            color_frequency[color] += 1
        else:
            color_frequency[color] = 1
    
    highest_val: int = 0
    high_key: str
    for elem in color_frequency:
        if color_frequency[elem] > highest_val:
            high_key = elem
            highest_val = color_frequency[elem]

    return color_frequency[high_key]


def count(input: list[str]) -> dict[str, int]:
    """Counts frequency of list items and returns a dictionary with those values."""
    frequency: dict[str, int] = {}

    for elem in input:
        if elem in frequency:
            frequency[elem] += 1
        else:
            frequency[elem] = 1
    
    return frequency


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Sorting items from input list by first letter, storing and returning the sort in a dictionary."""
    alphabetized: dict[str, list[str]] = {}

    for elem in input:
        letter: str = (elem[0, 1]).lower()
        alphabetized[letter].append(elem)


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Adding student to the day's attendance list."""
    attendance[day].append(student)
    return attendance