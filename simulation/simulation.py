"""
Top level representation of simulation
"""
from . import tools
from .sprite import Sprite


class Simulation:
    """
    Instance of this class represents siulated world
    """
    def __init__(self, func, mu=100, lamb=10):
        self.func = func
        self.mu = mu
        self.lamb = lamb
        self.sprites = list()
        self.initial_spawn()

    def run(self):
        pass # TODO

    def initial_spawn(self):
        mu = self.mu
        coord = tools.point_generator(seed=1, min_x=-3, min_y=-3, delta_x=6, delta_y=6)
        while mu:
            mu -= 1
            sprite = Sprite(*next(coord))
            self.sprites.append(sprite)

