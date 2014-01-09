"""
Wrapper for simulation class.
"""

import pygal
from time import sleep
from PySide.QtCore import QThread, Slot, Signal
from simulation.simulation import Simulation
from PySide.QtWebKit import *

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
        self.graphSize = 3

    def update_graph(self):
        """
        Function used to generate new graph and send appropiate signal to
        window.
        """
        min = self.simulation.population[0].x
        max = self.simulation.population[0].x
        self.graphname = self.graphtimer
        self.xy_chart = pygal.XY(stroke=False, show_legend = False, title_font_size = 27, label_font_size = 15, print_values = False)
        self.xy_chart.title = "Krok "+str(self.simulation.population[0].generation)+ " \t\t\t\t\tNajlepszy wynik: (" + str(self.simulation.population[0].x) + "," + str(self.simulation.population[0].y) + ") wartosc: " + str(self.simulation.population[0].value)
        self.i = 0
        if self.graphtimer == 0: 
            self.graphSize = 3
        while self.i < self.simulation.mi:
            if min > self.simulation.population[self.i].x:
                min = self.simulation.population[self.i].x
            if min > self.simulation.population[self.i].y:
                min = self.simulation.population[self.i].y
            if max < self.simulation.population[self.i].x:
                max = self.simulation.population[self.i].x
            if max < self.simulation.population[self.i].y:
                max = self.simulation.population[self.i].y

            self.xy_chart.add(str(self.i), [(self.simulation.population[self.i].x, self.simulation.population[self.i].y)])
            self.i = self.i + 1

        if min < 0:
            min = -min
        if max <0:
            max = -max
        if (min > max):
            max = min
        
        if max < self.graphSize :
            if max < self.graphSize-0.15:
                if self.graphSize > 0.8:
                    self.graphSize = self.graphSize-0.15

        self.xy_chart.add('Granica', [(self.graphSize, self.graphSize), (-self.graphSize, -self.graphSize)])

        GraphData = self.xy_chart.render()
        self.graph_changed.emit(GraphData)

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
        # TODO refresh graph

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
