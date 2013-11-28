"""
Window widget.
"""
from PySide import QtGui

class Window(QtGui.QMainWindow):
    """
    Main window frame.
    """

    labels = ['mi', 'lambda']
    def __init__(self, *args, **kwarg):
        super(Window, self).__init__(*args, **kwarg)

        widget = QtGui.QWidget()
        edits = self.EditWidget()
        edits.set_labels(self.labels)
        widget.addWidget(edits)

        self.setGeometry(100, 100, 600, 350)
        self.setCentralWidget(widget)
        self.setWindowTitle("E'voile")
        self.statusBar().showMessage('Ready')

        self.show()

    class EditWidget(QtGui.QWidget):
        """
        Widget used for handling input.
        """
        def __init__(self, *args, **kwarg):
            super(Window.EditWidget, self).__init__(*args, **kwarg)

            self.layout = QtGui.QFormLayout()

        def set_labels(self, labels):
            """
            Set label names in widget.
            """
            for label in labels:
                edit = QtGui.QLineEdit()
                self.layout.addRow(QtGui.QLabel(label), edit)

