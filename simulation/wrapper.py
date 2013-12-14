"""
Wrapper for simulation class.
"""

from PySide.QtCore import QThread, Slot, Signal
from simulation.simulation import Simulation

FUNCTION = lambda x1, x2: (4. * x1**2 - 2.1 * x1**4 + (1./3.) * x1**6 + \
                           x1 * x2 - 4 * x2**2 + 4 * x2**4 )
# TODO Check if synchronisation works.

class SimulationWrapper(QThread):
    """
    Control interface for simulation and separate thread used for running it.
    """

    graph_changed = Signal(object)  # TODO type needs to be precised
    updated = Signal(list)

    def __init__(self, parent=None):
        super(SimulationWrapper, self).__init__()#parent)
        self.simulation = None
        self.running = False

    def update_graph(self):
        """
        Function used to generate new graph and send appropiate signal to
        window.
        """
        pass  # TODO: make this

    @Slot(dict)
    def start(self, param):
        """
        Slot used to handle the event of starting the simulation.
        """
        if 'lambda' in param:
            param['lambda_'] = param['lambda']
            del param['lambda']
        if param:
            self.simulation = Simulation(FUNCTION, **param) # TODO missing arguments
        self.running = True
        super(SimulationWrapper, self).start()

    @Slot()
    def pause(self):
        """
        Slot used to handle the event of stopping the simulation.
        """
        self.running = False
        # TODO refresh graph

    @Slot()
    def continue_(self):
        """
        Slot used to handle the event of continuation of the simulation.
        """
        self.running = True
        super(SimulationWrapper, self).start()

    def run(self):
        if not self.simulation:
            raise ValueError("Simulation not initialised")

        while self.running and not self.simulation.condition():
            res = self.simulation.step()
            # TODO test this signal performance. May be quite a
            # bottleneck. This may be needed to be run every 0.2 second
            # or at least every 200 steps. Also, this function may need
            # minimal sleep after every step, for main thread to get
            # over control and deal with new events.
            self.updated.emit(res)

        if self.condition():
            self.running = False

    def __del__(self):
        self.running = False
        self.wait()

    def condition(self):
        return self.simulation.condition()
