#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
"""
Program finding function minimum using evolutionary algorithm.

By Andrzej Krzynówek, Wiktor Ślęczka & Radosław Więch
"""
from argparse import ArgumentParser

from simulation.simulation import Simulation

DESCRIPTION = "Program finding function minimum using evolutionary algorith"
FUNCTION = lambda x1, x2: (1./3.) * x1**6 - 2.1 * x1**4 + 4 * x1**2 \


def run(mu, lambde):
    sim = Simulation(FUNCTION, mu, lambde)
    sim.run()


if __name__ == "__main__":
    parser = ArgumentParser(description=DESCRIPTION)
    parser.add_argument("lambda", help="Number of children each parent spawns")
    parser.add_argument("mu", help="Number of parents taken into consideration when creating children")
    args = parser.parse_args()

