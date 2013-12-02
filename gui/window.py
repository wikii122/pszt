"""
Window widget.
"""
from PySide import QtGui
from gui.editwidget import EditWidget
from gui.graphwidget import GraphWidget


class Window(QtGui.QMainWindow):
    """
    Main window frame.
    """

    labels = ['mi', 'lambda']
    def __init__(self, *args, **kwarg):
        super(Window, self).__init__(*args, **kwarg)

        edits = EditWidget()
        edits.set_labels(self.labels)
        edits.setMaximumWidth(100)
        edits.show()

        graph = GraphWidget()
        graph.setMaximumWidth(500)
        graph.setMinimumWidth(500)
        graph.show()

        layout = QtGui.QHBoxLayout()
        layout.addWidget(edits)
        layout.addWidget(graph)

        widget = QtGui.QWidget()
        widget.setLayout(layout)
        widget.show()

        self.setGeometry(100, 100, 600, 350)
        self.setCentralWidget(widget)
        self.setWindowTitle("E'voile")
        self.statusBar().showMessage('Ready')



