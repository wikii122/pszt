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

    graph_changed = Signal(object)  # TODO type needs to be precised
    updated = Signal(list)
    simulation_end = Signal()

    def __init__(self, parent=None):
        super(SimulationWrapper, self).__init__()
        self.simulation = None
        self.running = False
        self.graphtimer = 0
        self.i = 0
        self.graphname = ''
    def update_graph(self):
        """
        Function used to generate new graph and send appropiate signal to
        window.
        """
        min = self.simulation.population[0].x
        max = self.simulation.population[0].x
        self.graphname = self.graphtimer
        self.xy_chart = pygal.XY(stroke=False)
        self.xy_chart.title = "najlepszy wynik: \n" + str(self.simulation.population[0].x) + ',' + str(self.simulation.population[0].y)
        self.i = 0
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
        #self.xy_chart.add('B', [(self.simulation.population[1].x, self.simulation.population[1].y)])
        if min < 0:
            min = -min
        if max <0:
            max = -max

	
        if min >= max:
            min = 1.1*min
            self.xy_chart.add('Granica', [(min, min), (-min, -min)])
        if min < max:
            max = 1.1*max
            self.xy_chart.add('Granica', [(max, max), (-max, -max)])

        self.xy_chart.render_to_file('taktaktak.svg')
        self.graph_changed.emit(self.graphname)
        #pass  # TODO: make this

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
        if not self.simulation:
            raise ValueError("Simulation not initialised")


        while self.running and not self.simulation.condition():
            res = self.simulation.step()
            #if self.graphtimer%3 == 1:
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