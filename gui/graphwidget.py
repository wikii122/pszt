"""
GUI element responsible for drawing and displaying graph.
"""
from PySide import QtGui

class GraphWidget(QtGui.QWidget):
    """
    Displays graph.
    Will provide interface in future.
    """
    def __init__(self, *args, **kwarg):
        super(GraphWidget, self).__init__(*args, **kwarg)
