"""
Contains Sprite class definition.
"""
# TODO remove relative import
from . import tools


class Sprite:
    """
    Represents the population member during simulation.
    """
    def __init__(self, x, y, fun, generation=0):
        self.x = x
        self.y = y
        self.fun = fun
        self.value = fun(x, y)
        self.generation = generation

    def spawn(self, lambda_):
        sprites = list()
        coord = tools.point_generator(min_x=-3, delta_x=6,
                                      min_y=-3, delta_y=6)
        while lambda_:
            lambda_ -= 1
            sprites.append(Sprite(*next(coord),
                                   fun=self.fun,
                                   generation=self.generation+1))
        return sprites

    # TODO: check comparisons
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
        return "({x}, {y}) => {val}".format(x=self.x, y=self.y, val=self.value)
