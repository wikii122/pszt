"""
Contains Sprite class definition.
"""
from simulation import tools
import math
import random

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
        
    def mutate(self):
        tauP = 1.0 / 2.0
        tau = 1.0 / math.sqrt(2.0 * math.sqrt(2.0))
        
        commonN = random.gauss(0, 1)
        xN = random.gauss(0, 1)
        yN = random.gauss(0, 1)
        
        self.deviationX *= math.exp(tauP * commonN + tau * xN)
        self.deviationY *= math.exp(tauP * commonN + tau * yN)
        
        self.x = self.x + self.deviationX * random.gauss(0, 1)
        self.y = self.y + self.deviationY * random.gauss(0, 1)
        
        self.value = self.fun(self.x, self.y)

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
