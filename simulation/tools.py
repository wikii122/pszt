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

def interpolate(a, x1, x2):
    """
    Calculates interpolated value between x1 and x2
    """
    return a * x1 + (1.0 - a) * x2

def apply_bounds(sprite):
    """
    Applies bounds to sprite's coordinates
    """
    if sprite.x < -2.0:
        sprite.x = -2.0
    elif sprite.x > 2.0:
        sprite.x = 2.0
        
    if sprite.y < -2.0:
        sprite.y = -2.0
    elif sprite.y > 2.0:
        sprite.y = 2.0