class Node:
    def __init__(self, x, y, fun):
        self.x = x
        self.y = y
        self.fun = fun

    def spawn(self):
        pass # TODO

    def value(self):
        return self.fun(self.x, self.y)
