"""
GUI element responsible for drawing and displaying graph.
"""
import pygal

from PySide import QtGui, QtCore, QtWebKit


class GraphWidget(QtGui.QWidget):
    def __init__(self, sim, parent=None):
        super(GraphWidget, self).__init__(parent)

        self.web = QtWebKit.QWebView()
        self.layout = QtGui.QVBoxLayout()

        self.layout.addWidget(self.web)
        self.setLayout(self.layout)
        self.initView()

        sim.graph_changed.connect(self.showgraph)

    @QtCore.Slot()
    def showgraph(self, data):
        qdata = QtCore.QByteArray(data)
        self.web.setContent(qdata)

    def initView(self):
        self.xy_chart = pygal.XY(stroke=False, show_legend = False, no_data_text = 'Enter parameters', title_font_size = 25)
        self.xy_chart.title = ("Projekt PSZT- Poszukiwanie Miniumum Funkcji")
        text_data = self.xy_chart.render()
        qdata = QtCore.QByteArray(text_data)
        self.web.setContent(qdata)

    @QtCore.Slot(str)
    def error(self, text):
        self.xy_chart = pygal.XY(stroke=False, show_legend = False, no_data_text = text, title_font_size = 25)
        self.xy_chart.title = ("Projekt PSZT- Poszukiwanie Miniumum Funkcji")
        text_data = self.xy_chart.render()
        qdata = QtCore.QByteArray(text_data)
        self.web.setContent(qdata)

