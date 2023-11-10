"""Simulating a river with all of my other classes!"""

__author__ = "730657997"

# are these unnecessary because they're imported in river, which is imported here?
# from exercises.ex08.fish import Fish
# from exercises.ex08.bear import Bear
from exercises.ex08.river import River


my_river: River = River(10, 2)
my_river.view_river()
my_river.one_river_week()