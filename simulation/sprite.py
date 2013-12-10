"""
Contains Sprite class definition.
"""
from simulation import tools


class Sprite:
    """
    Represents the population member during simulation.
    """
    def __init__(self, x, y, fun, deviationX, deviationY, generation=1):
        self.x = x
        self.y = y
        self.fun = fun
        self.value = fun(x, y)
        self.deviationX = deviationX
        self.deviationY = deviationY
        self.generation = generation

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __le__(self, other):
        return self.value <= other.value

    def __str__(self):
        return "({x:<20}, {y:<20}) => {val:<19}".format(x=self.x, y=self.y,
                                                        val=self.value)
    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value
