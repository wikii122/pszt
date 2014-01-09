"""
Wrapper for simulation class.
"""

import pygal

from time import sleep
from PySide.QtCore import QThread, Slot, Signal
from simulation.simulation import Simulation

FUNCTION = lambda x1, x2: (4. * x1**2 - 2.1 * x1**4 + (1./3.) * x1**6 + \
                           x1 * x2 - 4 * x2**2 + 4 * x2**4 )


class SimulationWrapper(QThread):
    """
    Control interface for simulation and separate thread used for running it.
    """

    graph_changed = Signal(object)
    updated = Signal(list)
    simulation_end = Signal()

    def __init__(self, parent=None):
        super(SimulationWrapper, self).__init__()
        self.simulation = None
        self.running = False

        self.graphtimer = 0
        self.graph_size = 3

    def update_graph(self):
        """
        Function used to generate new graph and send appropiate signal to
        window.
        """
        min_val = self.simulation.population[0].x
        max_val = self.simulation.population[0].x
        self.xy_chart = pygal.XY(stroke=False, show_legend = False, title_font_size = 27, label_font_size = 15, print_values = False)
        self.xy_chart.title = "Krok "+str(self.simulation.population[0].generation)+ " \t\t\t\t\tNajlepszy wynik: (" + str(self.simulation.population[0].x) + "," + str(self.simulation.population[0].y) + ") wartosc: " + str(self.simulation.population[0].value)
        i = 0
        if self.graphtimer == 0:
            self.graph_size = 3
        for member in self.simulation.population:
            if min_val > member.x:
                min_val = member.x
            if min_val > member.y:
                min_val = member.y
            if max_val < member.x:
                max_val = member.x
            if max_val < member.y:
                max_val = member.y

            self.xy_chart.add(str(i), [(member.x, member.y)])
            i = i + 1

        min_val = abs(min_val)
        max_val = abs(max_val)

        if (min_val > max_val):
            max_val = min_val

        if max_val < self.graph_size and max_val < self.graph_size-0.05 and self.graph_size > 0.8:
            self.graph_size = self.graph_size-0.05

        self.xy_chart.add('Granica', [(self.graphSize, self.graphSize), (-self.graphSize, -self.graphSize)])

        graph_data = self.xy_chart.render()
        self.graph_changed.emit(graph_data)

    @Slot(dict)
    def start(self, param):
        """
        Slot used to handle the event of starting the simulation.
        """
        if 'lambda' in param:
            param['lambda_'] = param['lambda']
            del param['lambda']
            self.simulation = Simulation(FUNCTION, **param)
        self.running = True
        super(SimulationWrapper, self).start()

    @Slot()
    def pause(self):
        """
        Slot used to handle the event of stopping the simulation.
        """
        self.running = False
        self.update_graph()

    @Slot()
    def continue_(self):
        """
        Slot used to handle the event of continuation of the simulation.
        """
        self.running = True
        super(SimulationWrapper, self).start()

    def run(self):
        self.graphtimer = 0
        if not self.simulation:
            raise ValueError("Simulation not initialised")


        while self.running and not self.simulation.condition():
            res = self.simulation.step()
            self.update_graph()
            self.graphtimer = self.graphtimer+1

            # TODO test this signal performance. May be quite a
            # bottleneck. This may be needed to be run every 0.2 second
            # or at least every 200 steps. Also, this function may need
            # minimal sleep after every step, for main thread to get
            # over control and deal with new events.
            self.updated.emit(res)
            sleep(0.1)

        if self.condition():
            self.running = False
            self.simulation_end.emit()

    def __del__(self):
        #self.running = False
        #self.wait()
        pass

    def condition(self):
        return self.simulation.condition()
