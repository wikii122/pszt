"""
Contains Sprite class definition.
"""
class Sprite:
    """
    Represents the population member during simulation.
    """
    def __init__(self, x, y, fun, generation=0):
        self.x = x
        self.y = y
        self.fun = fun(x, y)
        self.generation = generation

    def spawn(self):
        pass # TODO

    def value(self):
        return self.fun

    # TODO: check comparisons
    def __gt__(self, other):
        return self.fun > other.fun

    def __lt__(self, other):
        return self.fun < other.fun

    def __eq__(self, other):
        return self.fun == other.fun

    def __ge__(self, other):
        return self.fun >= other.fun

    def __le__(self, other):
        return self.fun <= other.fun

    def __str__(self):
        return "({x}, {y}) => {val}".format(x=self.x, y=self.y, val=self.fun)
