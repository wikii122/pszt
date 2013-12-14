"""
Widget used to handle edit fields.
"""
from time import sleep
from PySide import QtGui, QtCore
from simulation import Simulation


class EditWidget(QtGui.QWidget):
    """
    Widget used for handling input.
    """
    start_simulation = QtCore.Signal(dict)
    pause_simulation = QtCore.Signal()
    continue_simulation = QtCore.Signal()

    def __init__(self, sim=Simulation(), *args, **kwarg):
        super(EditWidget, self).__init__(*args, **kwarg)
        self.main_layout = QtGui.QVBoxLayout()
        self.edits = list()
        self.button = QtGui.QPushButton("&Run!", self)
        self.button.clicked.connect(self.push_button)
        self.labels = None
        self.run = False
        self.changed = True
        self.sim = sim

        self.start_simulation.connect(sim.start)
        self.pause_simulation.connect(sim.pause)
        self.continue_simulation.connect(sim.continue_)

        sim.finished.connect(self.finished)

    def set_labels(self, labels):
        """
        Set label names in widget.
        """
        self.layout = QtGui.QFormLayout()
        self.labels = labels
        for label in labels:
            edit = QtGui.QLineEdit()
            edit.setValidator(QtGui.QIntValidator(edit))
            edit.textChanged.connect(self.change)
            self.layout.addRow(QtGui.QLabel(label), edit)
            self.edits.append(edit)

    def change(self, _):
        """
        Invoked when parameters are changed.
        """
        self.changed = True
        if not self.run:
            self.button.setText("&Run!")
        sleep(0.1)

    def show(self):
        """
        Finalize layout and call QWidget.show() method.
        """
        self.main_layout.addLayout(self.layout)
        self.main_layout.addWidget(self.button)
        self.setLayout(self.main_layout)
        super(EditWidget, self).show()

    def push_button(self):
        """
        Executed when button is pushed
        """
        if not self.labels:
            raise Exception("Button pushed before GUI initialization finished")


        if not self.run:
            values = dict()

            if self.changed:
                # Start running with current parameters
                values = {x:int(y.text()) for x, y in zip(self.labels, self.edits)}
                for x in values:
                    if not values[x]:
                        # TODO make this more subtle.
                        QtGui.QMessageBox.question(self, 'Message', "Empty field!")
                        return

            self.run = True
            self.changed = False
            self.button.setText("&Stop!")
            self.start_simulation.emit(values)
            sleep(0.1)
        else:
            # Stop simulation without updating new parameters.
            self.run = False
            if not self.changed:
                self.button.setText("&Continue!")
            else:
                self.button.setText("&Run!")
            self.pause_simulation.emit()
            sleep(0.1)


    @QtCore.Slot()
    def finished(self):
        """
        Slot handling event of stopping simulation.
        """
        #pass  # TODO
        QtGui.QMessageBox.question(self, 'Message',
        "Are you sure to quit?", QtGui.QMessageBox.Yes |
                                 QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if self.sim.condition():
            self.run = False
            self.changed = True
            self.button.setText("&Run!")
            # TODO finalize process

