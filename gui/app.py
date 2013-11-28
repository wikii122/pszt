"""
Main application GUI handler.
"""
import sys

from PySide import QtGui

class Application(QtGui.QApplication):
    """
    Main application representation.
    """
    def __init__(self):
        super(Application, self).__init__(sys.argv)

        self.frame = Window()

    def run(self):
        """
        Starts the QT mainloop for application.
        """
        return self.exec_()

class Window(QtGui.QMainWindow):
    """
    Main window frame.
    """
    def __init__(self, *args, **kwarg):
        super(Window, self).__init__(*args, **kwarg)

        widget = QtGui.QWidget()

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

