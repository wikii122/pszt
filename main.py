#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
"""
Program finding function minimum using evolutionary algorithm.

By Andrzej Krzynówek, Wiktor Ślęczka & Radosław Więch
"""
from argparse import ArgumentParser
from simulation import Simulation

DESCRIPTION = "Program finding function minimum using evolutionary algorith"
FUNCTION = lambda x1, x2: (1./3.) * x1**6 - 2.1 * x1**4 + 4 * x1**2


def run(valmu, lambde):
    """
    Main function of program, it's used to create and start the simulation
    """
    print("Starting simulation with parameters \
          mu: {0} and lambda: {1}".format(valmu, lambde))
    sim = Simulation(FUNCTION, valmu, lambde)
    sim.run()


if __name__ == "__main__":
    parser = ArgumentParser(description=DESCRIPTION)
    parser.add_argument("lambda", type=int, help=\
                        "Number of children each parent spawns")
    parser.add_argument("mu", type=int, help=\
                        "Number of parents taken into consideration when \
                         creating children")
    args = parser.parse_args()

    run(args.mu, args.lambd)

