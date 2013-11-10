"""
Contains Sprite class definition.
"""
# TODO remove relative import
from . import tools


class Sprite:
    """
    Represents the population member during simulation.
    """
    def __init__(self, x, y, fun, generation=1):
        self.x = x
        self.y = y
        self.fun = fun
        self.value = fun(x, y)
        self.generation = generation

    def spawn(self, lambda_):
        sprites = list()
        delta = self.x/self.generation
        coord = tools.point_generator(min_x=self.x-delta, delta_x=2*delta,
                                      min_y=self.y-delta, delta_y=2*delta)
        while lambda_:
            lambda_ -= 1
            sprites.append(Sprite(*next(coord),
                                   fun=self.fun,
                                   generation=self.generation+1))
        return sprites

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
        return "({x:<19}, {y:<19}) => {val:<19}".format(x=self.x, y=self.y,
                                                    val=self.value)
    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value
