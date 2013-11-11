"""
Description of point
"""
import random

def point_generator(x, delta_x, y, delta_y):
    """
    Generator used to generate an infinite amount of
    pairs of points.
    """
    while True:
        d_x = random.random() * 2 * delta_x - delta_x
        d_y = random.random() * 2 * delta_y - delta_y
        return (x + d_x, y + d_y)

