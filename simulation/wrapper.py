"""
Wrapper for simulation class.
"""

from PySide.QtCore import QObject
from simulation.simulation import Simulation

class SimulationWrapper(QObject):
    """
    Control interface for simulation and separate thread used for running it.
    """
    def __init__(self):
        super(SimulationWrapper, self).__init__()
        self.simulation = None

    def start(self):
        """
        Function used to handle the signal of starting the simulation.
        """
        self.simulation = Simulation() # TODO missing arguments

    def pause(self):
        """
        Function used to handle the signal of stopping the simulation.
        """
        pass

    def continue_(self):
        """
        Function used to handle the signal of continuation of the simulation.
        """
        pass

    def _thread_run(self):
        pass
