"""Example functions to learn definition."""


def my_max(number1: int, number2: int) -> int:
    """Returns the maximum value out of two numbers."""
    if number1 >= number2:
        return number1
    else:
        return number2


max_number: int = my_max(1, 10)
other_max_number: int = my_max(11, 3)

print(other_max_number)