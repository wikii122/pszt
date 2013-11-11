"""
Contains Sprite class definition.
"""
# TODO remove relative import
from . import tools

_factor = 10

class Sprite:
    """
    Represents the population member during simulation.
    """
    def __init__(self, x, y, fun, range_, generation=_factor):
        self.x = x
        self.y = y
        self.fun = fun
        self.value = fun(x, y)
        self.generation = generation
        self.range = range_

    def spawn(self, lambda_):
        sprites = list()
        delta = self.range / self.generation * _factor
        coord = tools.point_generator(x=self.x, delta_x=delta,
                                      y=self.y, delta_y=delta)
        lambda_ -= 1
        sprites.append(Sprite(*next(coord),
                               fun=self.fun,
                               range_=self.range)
                      )
        while lambda_:
            lambda_ -= 1
            sprites.append(Sprite(*next(coord),
                                   fun=self.fun,
                                   range_=self.range,
                                   generation=self.generation+1)
                          )
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
        return "({x:<25}, {y:<25}) => {val:<19}".format(x=self.x, y=self.y,
                                                    val=self.value)
    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value
