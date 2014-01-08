"""
GUI element responsible for drawing and displaying graph.
"""
from PySide import QtGui, QtCore, QtWebKit
import pygal

import sys
from PySide.QtCore import QByteArray
from PySide.QtWebKit import QWebView


class GraphWidget(QtGui.QWidget):

    def __init__(self, sim, parent=None):
        super(GraphWidget, self).__init__(parent)
        sim.graph_changed.connect(self.showgraph)
        self.web = QWebView()
        self.layout = QtGui.QVBoxLayout();
        self.initView()


    @QtCore.Slot()
    def showgraph(self, data):
        Qdata = QByteArray(data)
        self.web.setContent(Qdata)
        self.layout.addWidget(self.web)
        self.setLayout(self.layout)

    def initView(self):
        self.xy_chart = pygal.XY(stroke=False, show_legend = False, no_data_text = '', title_font_size = 25)
        self.xy_chart.title = ("Projekt PSZT- Poszukiwanie Miniumum Funkcji")
        TextData = self.xy_chart.render()
        Qdata = QByteArray(TextData)
        self.web.setContent(Qdata)
        self.layout.addWidget(self.web)
        self.setLayout(self.layout)
