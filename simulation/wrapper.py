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
        self.minX = -3
        self.minY = -3
        self.maxX = 3
        self.maxY = 3
        self.generatedgraph = list()
        self.graphtype = 0


    def update_graph(self):
        """
        Function used to generate new graph and send appropiate signal to
        window.
        """

        localminX = localmaxX = self.simulation.population[0].x
        localminY = localmaxY = self.simulation.population[0].y

        for member in self.simulation.population:
            if localminX > member.x:
                localminX = member.x
            if localminY > member.y:
                localminY = member.y
            if localmaxX < member.x:
                localmaxX = member.x
            if localmaxY < member.y:
                localmaxY = member.y

        # Prevent point converging in corners
        if localmaxY > 0:
            localmaxY = 1.05 * localmaxY
        else:
            localmaxY = 0.95 * localmaxY

        if localmaxX > 0:
            localmaxX = 1.05 * localmaxX
        else:
            localmaxX = 0.95 * localmaxX

        if localminX < 0:
            localminX = 1.05 * localminX
        else:
            localminX = 0.95 * localminX

        if localminY < 0:
            localminY = 1.05 * localminY
        else:
            localminY = 0.95 * localminY

        # Fluent scaling
        deltaX = self.maxX*0.1
        deltaX = abs(deltaX)
        deltaY = self.maxY*0.1
        deltaY = abs(deltaY)

        if (self.maxX - deltaX) > localmaxX < self.maxX:
            self.maxX = self.maxX - deltaX
        if (self.maxY - deltaY) > localmaxY < self.maxY:
            self.maxY = self.maxY - deltaY
        if (self.minX + deltaX) < localminX > self.minX:
            self.minX = self.minX + deltaX
        if (self.minY + deltaY) < localminY > self.minY:
            self.minY = self.minY + deltaY

        if self.maxX < localminX or self.minX > localmaxX or self.maxY < localminY or self.minY > localmaxY:
            self.maxX = 1.5
            self.minX = -1.5
            self.maxY = 1.5
            self.minY = -1.5
        # calculating for "bar Chart"
        self.generatedgraph.append((self.simulation.population[0].generation, self.simulation.population[0].value))
        self.generatedgraph.append((self.simulation.population[-1].generation, self.simulation.population[-1].value))

        while (self.generatedgraph[-1][0] - self.generatedgraph[0][0]) > 21:
            self.generatedgraph = self.generatedgraph[1:]

        #calculating for X/Y chart

        if self.graphtype == 1 and (self.simulation.steps%3 == 0 or not self.running):
            self.xy_chart = pygal.XY(stroke=False, show_legend = False, title_font_size = 27, label_font_size = 10, print_values = False, human_readable = True)
            self.xy_chart.title = "Krok "+str(self.simulation.steps)+ " \t\t\t\t\tNajlepszy wynik: (" + str(self.simulation.population[0].x) + "," + str(self.simulation.population[0].y) + ") wartosc: " + str(self.simulation.population[0].value)
            points = list()
            for member in self.simulation.population:
                if self.minX < member.x < self.maxX and self.minY < member.y < self.maxY:
                    points.append((member.x, member.y))

            self.xy_chart.add('punkt', points)
            self.xy_chart.add('Granica', [(self.minX, self.minY), (self.maxX, self.maxY), (self.maxX, self.minY), (self.minX, self.maxY)])
            GraphData = self.xy_chart.render()
            self.graph_changed.emit(GraphData)


        #displaying second chart
        if self.graphtype == 0:
            self.barChart = pygal.XY( show_legend = False, title_font_size = 27, label_font_size = 10, print_values = False, human_readable = True)
            self.barChart.title = "Krok "+str(self.simulation.steps)+ " \t\t\t\t\tNajlepszy wynik: (" + str(self.simulation.population[0].x) + "," + str(self.simulation.population[0].y) + ") wartosc: " + str(self.simulation.population[0].value)
            i = 0
            while i < len(self.generatedgraph):
                self.barChart.add('punkty' , [(self.generatedgraph[i][0], self.generatedgraph[i][1]),(self.generatedgraph[i+1][0], self.generatedgraph[i+1][1])] )
                i = i+2
            GraphData = self.barChart.render()
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
            self.minX = -3
            self.minY = -3
            self.maxX = 3
            self.maxY = 3
            self.generatedgraph = []
            self.update_graph()
        self.running = True
        super(SimulationWrapper, self).start()

    @Slot(int)
    def changeType(self, newtype):
        self.graphtype = newtype
        if self.simulation:
            self.update_graph()

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
        if not self.simulation:
            raise ValueError("Simulation not initialised")


        while self.running and not self.simulation.condition():
            res = self.simulation.step(prints = False)
            self.update_graph()
            sleep(0.1)

        if self.condition():
            self.running = False
            #self.minX = self.minY = -3
            #self.maxX = self.maxX = 3
            self.simulation_end.emit()

        self.update_graph()

    def __del__(self):
        #self.running = False
        #self.wait()
        pass

    def condition(self):
        return self.simulation.condition()
