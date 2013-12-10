"""
Wrapper for simulation class.
"""

from PySide.QtCore import QThread
from simulation.simulation import Simulation

class SimulationWrapper(QThread):
    """
    Control interface for simulation and separate thread used for running it.
    """
    def __init__(self, parent=None):
        super(SimulationWrapper, self).__init__(parent)
        self.simulation = None
        self.exiting = False

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

    def run(self):
        if not self.simulation:
            raise ValueError("Simulation not initialised")
        while not self.exiting:
            self.simulation.step()
