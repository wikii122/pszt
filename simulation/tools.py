"""
Description of point
"""
import random

def point_generator(x, delta_x, y, delta_y, seed=None):
    """
    Generator used to generate an infinite amount of
    pairs of points.
    """
    if seed is not None:
        random.seed(seed)

    while True:
        d_x = random.random() * 2 * delta_x - delta_x
        d_y = random.random() * 2 * delta_y - delta_y
        yield (x + d_x, y + d_y)

