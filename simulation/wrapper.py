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
        self.running = False

    def start(self):
        """
        Function used to handle the signal of starting the simulation.
        """
        self.simulation = Simulation() # TODO missing arguments
        self.running = True
        super(SimulationWrapper, self).start()

    def pause(self):
        """
        Function used to handle the signal of stopping the simulation.
        """
        self.running = True

    def continue_(self):
        """
        Function used to handle the signal of continuation of the simulation.
        """
        self.running = False
        self.start()

    def run(self):
        if not self.simulation:
            raise ValueError("Simulation not initialised")
        while self.running:
            self.simulation.step()

    def __del__(self):
        self.running = False
        self.wait()  # TODO: Check if quitting correctly
