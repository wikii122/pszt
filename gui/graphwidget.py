"""
GUI element responsible for drawing and displaying graph.
"""
import sys
import pygal

from PySide import QtGui, QtCore, QtWebKit


class GraphWidget(QtGui.QWidget):

    def __init__(self, sim, parent=None):
        super(GraphWidget, self).__init__(parent)
        sim.graph_changed.connect(self.showgraph)
        self.web = QtWebKit.QWebView()
        self.layout = QtGui.QVBoxLayout();
        self.initView()


    @QtCore.Slot()
    def showgraph(self, data):
        qdata = QtCore.QByteArray(data)
        self.web.setContent(qdata)
        self.layout.addWidget(self.web)
        self.setLayout(self.layout)

    def initView(self):
        self.xy_chart = pygal.XY(stroke=False, show_legend = False, no_data_text = '', title_font_size = 25)
        self.xy_chart.title = ("Projekt PSZT- Poszukiwanie Miniumum Funkcji")
        TextData = self.xy_chart.render()
        qdata = QtCore.QByteArray(TextData)
        self.web.setContent(qdata)
        self.layout.addWidget(self.web)
        self.setLayout(self.layout)
