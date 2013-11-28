"""
Window widget.
"""
from PySide import QtGui
from gui.editwidget import EditWidget

class Window(QtGui.QMainWindow):
    """
    Main window frame.
    """

    labels = ['mi', 'lambda']
    def __init__(self, *args, **kwarg):
        super(Window, self).__init__(*args, **kwarg)

        edits = EditWidget()
        edits.set_labels(self.labels)
        edits.show()

        layout = QtGui.QHBoxLayout()
        layout.addWidget(edits)

        widget = QtGui.QWidget()
        widget.setLayout(layout)
        widget.show()

        self.setGeometry(100, 100, 600, 350)
        self.setCentralWidget(widget)
        self.setWindowTitle("E'voile")
        self.statusBar().showMessage('Ready')



