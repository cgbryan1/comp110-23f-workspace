"""File to define Bear class."""

__author__ = "730657997"


class Bear:
    """Bears!"""
    
    age: int
    hunger_score: int

    def __init__(self):
        """Initiating a bear object, setting age and hunger to 0."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Each day that passes, a bear ages by 1 and their hunger goes down by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """A bear's hunger score is increased by the fish they eat."""
        self.hunger_score += num_fish
        return None