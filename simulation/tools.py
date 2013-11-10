"""
Description of point
"""
import random

def point_generator(min_x, delta_x, min_y, delta_y, seed=None):
    """
    Generator used to generate an infinite amount of
    pairs of points.
    """
    if seed is not None:
        random.seed(seed)

    while True:
        x = random.random() * delta_x - delta_x/2
        y = random.random() * delta_y - delta_y/2
        yield (min_x + x, min_y + y)

