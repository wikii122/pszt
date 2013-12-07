"""
Wrapper for simulation class.
"""

from PySide.QtCore import QObject

class SimulationWrapper(QObject):
    """
    Control interface for simulation.
    """
    def __init__(self):
        super(SimulationWrapper, self).__init__()

