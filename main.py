#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
"""
Program finding function minimum using evolutionary algorithm.

By Andrzej Krzynówek, Wiktor Ślęczka & Radosław Więch
"""
import os
import sys
import random

from argparse import ArgumentParser

path = os.path.dirname(sys.argv[0])
path = os.path.abspath(path)
sys.path.append(path)

from simulation import Simulation
from gui.app import Application

DESCRIPTION = "Program finding function minimum using evolutionary algorithm"
FUNCTION = lambda x1, x2: (4. * x1**2 - 2.1 * x1**4 + (1./3.) * x1**6 + \
                           x1 * x2 - 4 * x2**2 + 4 * x2**4 )

def run():
    """
    Main function of program, it's used to create and start the simulation
    """
    sim = Simulation(FUNCTION)
    app = Application(sim)
    app.run()

if __name__ == "__main__":
    parser = ArgumentParser(description=DESCRIPTION)
    parser.add_argument("--debug", action="store_true", help=\
                        "Use fixed seed for random generator")

    args = parser.parse_args()
    if args.debug:
        random.seed(1)

    run()
