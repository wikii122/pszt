#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
"""
Program finding function minimum using evolutionary algorithm.

By Andrzej Krzynówek, Wiktor Ślęczka & Radosław Więch
"""
import sys

from argparse import ArgumentParser
from simulation import Simulation

DESCRIPTION = "Program finding function minimum using evolutionary algorithm"
FUNCTION = lambda x1, x2: (4. * x1**2 - 2.1 * x1**4 + (1./3.) * x1**6 + \
                           x1 * x2 - 4 * x2**2 + 4 * x2**4 )


def run(mi, lambda_, prints=True):
    """
    Main function of program, it's used to create and start the simulation
    """
    if mi <= 1 or lambda_ <= 1:
        print("Parameters must be greater than 1")
        sys.exit(1)
    if prints:
        print("Starting simulation with parameters \
               mu: {0} and lambda: {1}".format(mi, lambda_))
    sim = Simulation(FUNCTION, mi, lambda_)
    res = sim.run(prints)

    return res

def test(mi, lambda_):
    bad = []
    for x in range(2, args.mi):
        for y in range(2, getattr(args, "lambda")):
            res = run(x, y, False)
            if res.value > -1.03:
                print("Mi: {mi:<3}, lambda: {lambda_:<3} => {val}"
                     .format(mi=x, lambda_=y, val=res.value))
                bad.append((x, y))
    print(bad)

if __name__ == "__main__":
    parser = ArgumentParser(description=DESCRIPTION)
    parser.add_argument("lambda", type=int, help=\
                        "Number of children each parent spawns")
    parser.add_argument("mi", type=int, help=\
                        "Number of parents taken into consideration when \
                         creating children")
    #TODO Remove in final
    parser.add_argument("--test", action="store_true", help=\
                        "Run for every combination of parameters less \
                         than given")
    args = parser.parse_args()
    # Getting attribute manually due to name clash.
    if args.test:
        test(args.mi, getattr(args, "lambda"))
    else:
        run(args.mi, getattr(args, "lambda"))
