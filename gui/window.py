"""
Window widget.
"""
from PySide import QtGui, QtCore
from gui.editwidget import EditWidget
from gui.graphwidget import GraphWidget


class Window(QtGui.QMainWindow):
    """
    Main window frame.
    """

    labels = ['mi', 'lambda']
    size = (600, 350)
    def __init__(self, simulation):
        super(Window, self).__init__()

        edits = EditWidget(sim=simulation, parent=self, status=self.statusBar())
        edits.set_labels(self.labels)
        edits.setMaximumWidth(150)
        edits.show()

        graph = GraphWidget(sim=simulation, parent=self)
        graph.setMaximumWidth(450)
        graph.setMinimumWidth(450)
        graph.show()

        layout = QtGui.QHBoxLayout()
        layout.addWidget(edits)
        layout.addWidget(graph)

        widget = QtGui.QWidget()
        widget.setLayout(layout)
        widget.show()

        self.setGeometry(100, 100, *self.size)
        self.setCentralWidget(widget)
        self.setWindowTitle("E'voile")
        self.statusBar().showMessage('Ready')

    def show(self):
        super(Window, self).show()
        size = QtCore.QSize(*self.size)
        self.setFixedSize(size)
