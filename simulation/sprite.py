class Sprite:
    def __init__(self, x, y, fun, generation=0):
        self.x = x
        self.y = y
        self.fun = fun(x, y)
        self.generation = generation

    def spawn(self):
        pass # TODO

    def value(self):
        return self.fun
