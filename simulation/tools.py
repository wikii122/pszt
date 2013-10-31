"""
Description of point
"""
import random

def point_generator(seed, min_x, delta_x, min_y, delta_y):
    """
    TODO
    """
    random.seed(seed)
    while True:
        x = random.random() * delta_x
        y = random.random() * delta_y
        yield (min_x + x, min_y + y)

def log(fun):
    def log_wrapper(*args, **kw):
        print(args)
        ret = fun(*args, **kw)
        print(ret)
    return log_wrapper
