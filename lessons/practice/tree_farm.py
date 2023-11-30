"""Practice class writing for Quiz 3."""

class ChristmasTreeFarm:
    plots: list[int]


    def __init__(self, plots: int, initial_planting: int):
        """Initializing with x number of plots and x planted trees."""
        self.plots = []
        existing_plots: int = 0
        for value in initial_planting:
            if value > 0:
                self.plots.append(value)
                existing_plots += 1

        while existing_plots < plots:
            self.plots.append(0)
            existing_plots +=1


    def plant(self, plot_idx: int) -> None:
        """Plant a new tree at specified index."""
        self.plots[plot_idx] = 1


    def growth(self) -> None:
        """Grow each planted tree by 1."""
        for value in self.plots:
            if value > 1:
                value += 1
    

    def harvest(self, replant: bool) -> int:
        """Harvest trees and decide whether to replant."""
        harvested: int =  0
        for value in self.plots:
            if value >= 5:
                harvested += 1
                if replant:
                    value = 1
                else:
                    value = 0
        return harvested
    
    def __add__(self, other: ChristmasTreeFarm) -> ChristmasTreeFarm:
        """Overloading to combine two farms."""
        new: ChristmasTreeFarm = ChristmasTreeFarm(0, 0)

        for value in self.plots:
            new.plots.append(value)
        
        for value in other.plots:
            new.plots.append(value)
        
        return new

