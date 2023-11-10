"""File to define Fish class."""

__author__ = "730657997"


class Fish:
    """Creating fish!"""
    age: int

    def __init__(self):
        """Constructor for fish objects, setting age equal to zero."""
        self.age = 0
        return None
    
    def one_day(self):
        """Each day that passes, the fish age by 1."""
        self.age += 1
        return None