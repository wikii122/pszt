"""
Top level representation of simulation.
"""
#TODO: remove relative imports
from . import tools
from .sprite import Sprite


class Simulation:
    """
    Instance of this class represents simulated world
    """
    def __init__(self, func, mi=100, lamb=10):
        self.func = func
        self.mi = mi
        self.lamb = lamb
        self.population = list()
        self.initial_spawn()
        self.steps = 0

    def run(self):
        while self:
            self.step()
        
        print("Solution {solution}".format(solution=self.population[0]))

    def initial_spawn(self):
        mi = self.mi
        coord = tools.point_generator(seed=1,
                                      min_x=-3, delta_x=6,
                                      min_y=-3, delta_y=6)
        while mi:
            mi -= 1
            sprite = Sprite(*next(coord), fun=self.func)
            self.population.append(sprite)

    def step(self):
        self.steps += 1
        sprites = list()

        for sprite in self.population:
            sprites += sprite.spawn(self.lamb, self.steps)

        sprites = sorted(sprites)
        self.population = sprites[:self.mi]

        print("Step {step}:".format(step=self.steps))
        for sprite in self.population:
            print(str(sprite))

    def __bool__(self):
        # TODO here should be finish condition.
         
        epsilon = 0.0001
        delta = abs(self.population[0] - self.population[-1])
        if delta < epsilon:
            return False
        
        return True
