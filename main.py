#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
"""
Program finding function minimum using evolutionary algorithm.

By Andrzej KrzynĂłwek, Wiktor ĹšlÄ™czka & RadosĹ‚aw WiÄ™ch
"""
from argparse import ArgumentParser
from simulation import Simulation

DESCRIPTION = "Program finding function minimum using evolutionary algorith"
FUNCTION = lambda x1, x2: (4. * x1**2 - 2.1 * x1**4 + (1./3.) * x1**6 + \
                           x1 * x2 - 4 * x2**2 + 4 * x2**4 )


def run(valmi, lambde):
    """
    Main function of program, it's used to create and start the simulation
    """
    print("Starting simulation with parameters \
          mu: {0} and lambda: {1}".format(valmi, lambde))
    sim = Simulation(FUNCTION, valmi, lambde)
    sim.run()


if __name__ == "__main__":
    parser = ArgumentParser(description=DESCRIPTION)
    parser.add_argument("lambda", type=int, help=\
                        "Number of children each parent spawns")
    parser.add_argument("mi", type=int, help=\
                        "Number of parents taken into consideration when \
                         creating children")
    args = parser.parse_args()
    # Getting attribute manually due to name clash.
    run(args.mi, getattr(args, "lambda"))
