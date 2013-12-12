"""
Top level representation of simulation.
"""
from simulation import tools
from simulation.sprite import Sprite
import random

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
        while mi:
            coord = tools.point_generator(x=0, delta_x=3,
                                          y=0, delta_y=3)
            mi -= 1
            sprite = Sprite(*coord, fun=self.func, deviationX=10, deviationY=10)
            self.population.append(sprite)

    def step(self, prints=True):
        self.steps += 1
        
        sprites = self.crossover()
        sprites = self.mutate(sprites)
        
        sprites = sorted(sprites)
        self.population = sprites[:self.mi]

        if not self.steps % 10 and prints:
            print("Step {step}:".format(step=self.steps))
            print(str(self.population[0]))

    def condition(self):
        return abs(self.population[0] - self.population[-1]) < self.epsilon
        
    def crossover(self):
        sprites = list()
        i = self.lambda_
        
        while i > 0:
            j = random.randint(0, len(self.population)-1)
            k = j
            while k == j:
                k = random.randint(0, len(self.population)-1)
            a = random.random()
            x = tools.interpolate(a, self.population[j].x, self.population[k].x) 
            y = tools.interpolate(a, self.population[j].y, self.population[k].y)
            deviationX = tools.interpolate(a, self.population[j].deviationX,
                                            self.population[k].deviationX)
            deviationY = tools.interpolate(a, self.population[j].deviationY, 
                                            self.population[k].deviationY)
            
            sprite = Sprite(x, y, self.func, deviationX, deviationY, 
                            self.population[j].generation+1)
            
            sprites.append(sprite)
            
            i = i - 1
            
        return sprites
        
    def mutate(self, sprites):
        
        for sprite in sprites:
            sprite.mutate()
            
        return sprites
            
