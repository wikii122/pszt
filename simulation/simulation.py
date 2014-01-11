"""
Top level representation of simulation.
"""
import random

from simulation import tools
from simulation.sprite import Sprite

class Simulation:
    """
    Instance of this class represents simulated world
    """
    def __init__(self, func, mi=100, lambda_=10):
        mi, lambda_ = map(int, [mi, lambda_])
        if mi <= 1 or lambda_ <= 1:
            raise ValueError("Unsupported parameters")

        self.func = func
        self.mi = mi
        self.lambda_ = lambda_
        self.population = list()
        self.initial_spawn()
        self.steps = 0
        self.epsilon = 0.00001
        self.mutation_chance = 0.05

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
        while mi:
            coord = tools.point_generator(x=0, delta_x=2,
                                          y=0, delta_y=2)
            mi -= 1
            sprite = Sprite(*coord, fun=self.func, deviationX=0.5, deviationY=0.5)
            self.population.append(sprite)
            self.population = sorted(self.population)


    def step(self, prints=True):
        self.steps += 1

        sprites = self.create_new_population()
        sprites = self.crossover(sprites)
        sprites = self.mutate(sprites)
        sprites = sorted(sprites)

        self.population = sprites[:self.mi]

        if not self.steps % 10 and prints:
            print("Step {step}:".format(step=self.steps))
            print(str(self.population[0]))

    def condition(self):
        return abs(self.population[0] - self.population[-1]) < self.epsilon

    def create_new_population(self):
        i = self.lambda_
        sprites = list()

        while i > 0:
            j = random.randint(0, len(self.population) - 1)
            sprites.append(self.population[j])
            i -= 1

        return sprites

    def crossover(self, population):
        sprites = list()
        population_idx = 0

        for member in population:
            a = random.random()

            """
            there are n-2 possible slots to select sprite to crossover with,
            but randomized value can only be used as index if its less than
            currently processed index, if its equal or higher then we have to
            normalize it by adding 1 to match full range of index values
            """
            i = random.randint(0, len(self.population) - 2)

            if (i >= population_idx):
                i += 1

            x = tools.interpolate(a, member.x, population[i].x)
            y = tools.interpolate(a, member.y, population[i].y)

            deviationX = tools.interpolate(a, member.deviationX,
                                        population[i].deviationY)
            deviationY = tools.interpolate(a, member.deviationY,
                                        population[i].deviationY)

            sprite = Sprite(x, y, self.func, member.deviationX, member.deviationY,
                            member.generation + 1)

            tools.apply_bounds(sprite)
            sprites.append(sprite)

            population_idx += 1

        return sprites

    def mutate(self, sprites):
        for sprite in sprites:
            if random.random() < self.mutation_chance:
                sprite.mutate()


        return sprites

