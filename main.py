#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
"""
Program finding function minimum using evolutionary algorithm.

By Andrzej Krzynówek, Wiktor Ślęczka & Radosław Więch
"""
import sys
import random

from argparse import ArgumentParser
from simulation import Simulation

DESCRIPTION = "Program finding function minimum using evolutionary algorithm"
FUNCTION = lambda x1, x2: (4. * x1**2 - 2.1 * x1**4 + (1./3.) * x1**6 + \
                           x1 * x2 - 4 * x2**2 + 4 * x2**4 )


def run(mi, lambda_):
    """
    Main function of program, it's used to create and start the simulation
    """
    if mi <= 1 or lambda_ <= 1:
        print("Parameters must be greater than 1")
        sys.exit(1)
    print("Starting simulation with parameters \
           mu: {0} and lambda: {1}".format(mi, lambda_))
    sim = Simulation(FUNCTION, mi, lambda_)
    sim.run()

if __name__ == "__main__":
    parser = ArgumentParser(description=DESCRIPTION)
    parser.add_argument("lambda", type=int, help=\
                        "Number of children each parent spawns")
    parser.add_argument("mi", type=int, help=\
                        "Number of parents taken into consideration when \
                         creating children")
    parser.add_argument("--debug", action="store_true", help=\
                        "Use fixed seed for random generator")

    args = parser.parse_args()
    if args.debug:
        random.seed(1)
    # Getting attribute manually due to name clash.
    run(args.mi, getattr(args, "lambda"))
