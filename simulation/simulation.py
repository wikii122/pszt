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
    def __init__(self, func, mi=100, lambda_=10):
        if mi <= 1 or lambda_ <= 1:
            raise ValueError("Unsupported parameters")

        self.func = func
        self.mi = mi
        self.lambda_ = lambda_
        self.population = list()
        self.initial_spawn()
        self.steps = 0
        self.epsilon = 0.000001

    def run(self, prints=True):
        while not self.condition():
            self.step(prints)

        if prints:
            print("Simulation finished after {step} generations\n"
                  "Solution {solution}".format(solution=self.population[0],
                                               step=self.steps))
        return self.population[0]

    def initial_spawn(self):
        mi = self.mi
        coord = tools.point_generator(seed=1,
                                      min_x=-3, delta_x=3,
                                      min_y=-3, delta_y=3)
        while mi:
            mi -= 1
            sprite = Sprite(*next(coord), fun=self.func)
            self.population.append(sprite)

    def step(self, prints=True):
        self.steps += 1
        sprites = list()

        for sprite in self.population:
            sprites += sprite.spawn(self.lambda_)

        sprites = sorted(sprites)
        self.population = sprites[:self.mi]

        if not self.steps % 10 and prints:
            print("Step {step}:".format(step=self.steps))
            for sprite in self.population:
                print(str(sprite))

    def condition(self):
        return abs(self.population[0] - self.population[-1]) < self.epsilon
