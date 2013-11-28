"""
Main application GUI handler.
"""
import sys

from PySide import QtGui
from gui.window import Window


class Application(QtGui.QApplication):
    """
    Main application representation.
    """
    def __init__(self):
        super(Application, self).__init__(sys.argv)
        self.frame = Window()
        self.frame.show()

    def run(self):
        """
        Starts the QT mainloop for application.
        """
        return self.exec_()
