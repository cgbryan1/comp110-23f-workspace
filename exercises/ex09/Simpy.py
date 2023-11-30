"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730657997"


class Simpy:
    """EX09 assignment."""
    
    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, input: list[float]):
        """Initializing a Simpy object."""
        self.values = input

    def __str__(self) -> str:
        """Magic method to return a string."""
        return (f"Simpy({self.values})")
    
    def fill(self, filler: float, num_vals: int) -> None:
        """Fills a Simpy's values with a specific number of repeating values."""
        i: int = 0
        new_list: list[float] = list()
        while i < num_vals:
            new_list.append(filler)
            i += 1
        
        self.values = new_list
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in values  with range of values in terms of floats."""
        assert step != 0.0

        range: list[float] = list()
        val: float = start

        while abs(val) < abs(stop):
            range.append(val)
            val += step

        self.values = range
    
    def sum(self) -> float:
        """Adds all values in the object's list."""
        return float(sum(self.values))
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adding together two lists' values or adding float to all idxs."""
        # Union type??? Hello??? I thought int | str
        listy: list[float] = list()
        new_simpy: Simpy = Simpy(listy)

        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            for idx in range(0, len(self.values)):
                new_simpy.values.append(self.values[idx] + rhs.values[idx])
        else:
            for idx in range(0, len(self.values)):
                new_simpy.values.append(self.values[idx] + rhs)

        return new_simpy
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Multiplying list vaues by corresponding idx or float."""
        # Union type??? Hello??? I thought int | str
        listy: list[float] = list()
        new_simpy: Simpy = Simpy(listy)

        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            for idx in range(0, len(self.values)):
                new_simpy.values.append(self.values[idx] ** rhs.values[idx])
        else:
            for idx in range(0, len(self.values)):
                new_simpy.values.append(self.values[idx] ** rhs)

        return new_simpy
  
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produce a list saying which values match."""
        bool_list: list[bool] = list()
        
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            for idx in range(0, len(self.values)):
                if self.values[idx] == rhs.values[idx]:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
        else:
            for idx in range(0, len(self.values)):
                if self.values[idx] == rhs:
                    bool_list.append(True)
                else:
                    bool_list.append(False)

        return bool_list
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produce a list saying which values are greater."""
        bool_list: list[bool] = list()
        
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            for idx in range(0, len(self.values)):
                if self.values[idx] > rhs.values[idx]:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
        else:
            for idx in range(0, len(self.values)):
                if self.values[idx] > rhs:
                    bool_list.append(True)
                else:
                    bool_list.append(False)

        return bool_list
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Subscription notation."""        
        if type(rhs) is int:
            return self.values[rhs]
        else:
            mask_list: list[float] = list()
            
            for idx in range(0, len(rhs)):
                # assert len(rhs) == len(self.values)
                if rhs[idx] is True:
                    mask_list.append(self.values[idx])
            
            mask: Simpy = Simpy(mask_list)
            return mask