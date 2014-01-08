"""
GUI element responsible for drawing and displaying graph.
"""
from PySide import QtGui, QtCore
import pygal

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *


class GraphWidget(QtGui.QWidget):

    #xy_chart = pygal.XY(stroke=False)
    
    def __init__(self, sim, parent=None):
        super(GraphWidget, self).__init__(parent)
        sim.graph_changed.connect(self.showgraph)
        self.web = QWebView()
        self.layout = QtGui.QVBoxLayout();


    @QtCore.Slot()
    def showgraph(self):
        self.web.load(QUrl("/home/radek/pszt/taktaktak.svg"))
        #self.web.show() 
        self.layout.addWidget(self.web)
        self.setLayout(self.layout)
        super(GraphWidget, self).show()
        #self.xy_chart.render_to_file('taktaktak.svg')

