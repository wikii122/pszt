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

        self.setGeometry(100, 100, 600, 350)
        self.setWindowTitle("E'volie")
        self.statusBar().showMessage('Ready')

        self.show()
