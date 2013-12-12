"""
Wrapper for simulation class.
"""

from PySide.QtCore import QThread, Slot, Signal
from simulation.simulation import Simulation

class SimulationWrapper(QThread):
    """
    Control interface for simulation and separate thread used for running it.
    """

    graph_changed = Signal(object)  # TODO type needs to be precised

    def __init__(self, parent=None):
        super(SimulationWrapper, self).__init__(parent)
        self.simulation = None
        self.running = False

    def update_graph(self):
        """
        Function used to generate new graph and send appropiate signal to
        window.
        """
        pass  # TODO: make this

    @Slot()
    def start(self):
        """
        Function used to handle the signal of starting the simulation.
        """
        self.simulation = Simulation() # TODO missing arguments
        self.running = True
        super(SimulationWrapper, self).start()

    @Slot()
    def pause(self):
        """
        Function used to handle the signal of stopping the simulation.
        """
        self.running = True

    @Slot()
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
