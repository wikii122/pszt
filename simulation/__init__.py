"""
Algorithm and simulation helpers for evolutionary algorithm.
"""
from simulation import wrapper

__all__ = ['Simulation']
# It isn't pretty, but backward compatible and clear - what we want
# outside is only
Simulation = wrapper.SimulationWrapper
