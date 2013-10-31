#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
"""
Program finding function minimum using evolutionary algorithm.

By Andrzej Krzynówek, Wiktor Ślęczka & Radosław Więch
"""
from argparse import ArgumentParser

DESCRIPTION = "Program finding function minimum using evolutionary algorith"
FUNCTION = lambda x1, x2: (1./3.) * x1**6 - 2.1 * x1**4 + 4 * x1**2 \
                        + 4 * x2**4 - 4 * x2**2 + x1 * x2

if __name__ == "__main__":
    parser = ArgumentParser(description=DESCRIPTION)
    args = parser.parse_args()
