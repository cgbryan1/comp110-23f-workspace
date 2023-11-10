"""File to define River class."""

__author__ = "730657997"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Creating a river!"""
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Making a new list of surviving animals and reassigning it to the og list."""
        surviving_bears: list[Bear] = []
        for idx in range(0, len(self.bears)):
            # for each bear in list, check if age is <= 5
            if self.bears[idx].age <= 5:
                surviving_bears.append(self.bears[idx])

        self.bears = surviving_bears

        surviving_fish: list[Fish] = []
        for idx in range(0, len(self.fish)):
            # for each fish in list, check if age is <= 3
            if self.fish[idx].age <= 3:
                surviving_fish.append(self.fish[idx])

        self.fish = surviving_fish
        
        return None

    def remove_fish(self, amount: int):
        """Removes input amount of fish from river, starting at idx 0."""
        remaining: list[Fish] = []
        for idx in range(amount, len(self.fish)):
            remaining.append(self.fish[idx])
        
        self.fish = remaining
        return None

    def bears_eating(self):
        """For each Bear, if there are at least 5 Fish in the river, the Bear will eat 3 Fish."""
        # self fish isn't working :(
        for key in self.bears:
            if len(self.fish) >= 4:
                self.fish.remove_fish(3)
                self.bears[key].eat(3)
    
    def check_hunger(self):
        """If a bear's hunger score is below zero, then the Bear dies."""
        survivors: list[Bear] = []
        for idx in range(0, len(self.bears)):
            if self.bears[idx].hunger_score > 0:
                survivors.append(self.bears[idx])
        
        self.bears = survivors

    def repopulate_fish(self):
        """For every 2 fish, they will have 4 kids."""
        num_fish: int = len(self.fish) - 1
        offspring: int = num_fish * 2
        
        idx: int = 0
        while idx < offspring:
            new_fish: Fish = Fish()
            self.fish.append(new_fish)
            idx += 1
    
    def repopulate_bears(self):
        """For every 2 bears, they will have 1 child."""
        num_bears: int = len(self.bears) - 1
        offspring: int = num_bears / 2
        
        idx: int = 0
        while idx < offspring:
            new_bear: Bear = Bear()
            self.bears.append(new_bear)
            idx += 1
    
    def view_river(self):
        """Making the output pretty."""
        to_print: str = f"~~~ Day {self.day}: ~~~\n"
        to_print += f"Fish population: {len(self.fish)}\n"
        to_print += f"Bear population: {len(self.bears)}\n"
        print(to_print)
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Simulates a week by calling the day function 7 times."""
        # did i do this wrong? no output
        x: int = 0
        while x < 7:
            self.one_river_day()