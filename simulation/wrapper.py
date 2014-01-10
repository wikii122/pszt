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
        self.minX = -3
        self.minY = -3
        self.maxX = 3
        self.maxY = 3

    def update_graph(self):
        """
        Function used to generate new graph and send appropiate signal to
        window.
        """
        localminX = localmaxX = self.simulation.population[0].x
        localminY = localmaxY = self.simulation.population[0].y
        self.xy_chart = pygal.XY(stroke=False, show_legend = False, title_font_size = 27, label_font_size = 10, print_values = False, human_readable = True)
        self.xy_chart.title = "Krok "+str(self.simulation.population[0].generation)+ " \t\t\t\t\tNajlepszy wynik: (" + str(self.simulation.population[0].x) + "," + str(self.simulation.population[0].y) + ") wartosc: " + str(self.simulation.population[0].value)
        self.i = 0

        while self.i < self.simulation.mi:
            if localminX > self.simulation.population[self.i].x:
                localminX = self.simulation.population[self.i].x
            if localminY > self.simulation.population[self.i].y:
                localminY = self.simulation.population[self.i].y
            if localmaxX < self.simulation.population[self.i].x:
                localmaxX = self.simulation.population[self.i].x
            if localmaxY < self.simulation.population[self.i].y:
                localmaxY = self.simulation.population[self.i].y
            #self.xy_chart.add(str(self.i), [(self.simulation.population[self.i].x, self.simulation.population[self.i].y)])
            self.i = self.i + 1

        if localmaxX < self.maxX:
            if localmaxY < self.maxY:
                if localminX > self.minX:
                    if localminY > self.minY:
                        self.maxX = self.maxX - (self.maxX - localmaxX)/2
                        self.maxY = self.maxY - (self.maxY - localmaxY)/2
                        self.minX = self.minX + (localminX - self.minX)/2
                        self.minY = self.minY + (localminY - self.minY)/2
        self.i = 0

        while self.i < self.simulation.mi:
            if self.minX < self.simulation.population[self.i].x < self.maxX and self.minY < self.simulation.population[self.i].y < self.maxY:
                self.xy_chart.add(str(self.i), [(self.simulation.population[self.i].x, self.simulation.population[self.i].y)])
            self.i = self.i + 1
        self.xy_chart.add('Granica', [(self.minX, self.minY), (self.maxX, self.maxY), (self.maxX, self.minY), (self.minX, self.maxY)])

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
            res = self.simulation.step()
            self.minX = -3
            self.minY = -3
            self.maxX = 3
            self.maxY = 3
            self.update_graph()
            self.updated.emit(res)
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
            self.update_graph()
            
            # TODO test this signal performance. May be quite a
            # bottleneck. This may be needed to be run every 0.2 second
            # or at least every 200 steps. Also, this function may need
            # minimal sleep after every step, for main thread to get
            # over control and deal with new events.
            self.updated.emit(res)
            sleep(0.1)

        if self.condition():
            self.running = False
            #self.minX = self.minY = -3
           # self.maxX = self.maxX = 3
            self.simulation_end.emit()

    def __del__(self):
        #self.running = False
        #self.wait()
        pass

    def condition(self):
        return self.simulation.condition()
