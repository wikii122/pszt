"""
Widget used to handle edit fields.
"""
from time import sleep
from PySide import QtGui, QtCore


class EditWidget(QtGui.QWidget):
    """
    Widget used for handling input.
    """
    start_simulation = QtCore.Signal(dict)
    pause_simulation = QtCore.Signal()
    continue_simulation = QtCore.Signal()

    def __init__(self, sim, parent=None, status=None):
        super(EditWidget, self).__init__(parent=parent)
        self.main_layout = QtGui.QVBoxLayout()
        self.edits = list()
        self.button = QtGui.QPushButton("&Run!", self)
        self.button.clicked.connect(self.push_button)
        self.labels = None
        self.run = False
        self.changed = True
        self.status = status

        self.start_simulation.connect(sim.start)
        self.pause_simulation.connect(sim.pause)
        self.continue_simulation.connect(sim.continue_)
        self.destroyed.connect(sim.terminate)

        sim.simulation_end.connect(self.finished)

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
            if self.status:
                self.status.showMessage("Ready")
        sleep(0.001)

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
            # Actually, this can be written a lot prettier
            values = dict()
            if self.changed:
                # Start running with current parameters
                try:
                    values = {x:float(y.text()) for x, y in zip(self.labels, self.edits)}
                except ValueError:
                    # TODO: Display error message  in place of result display.
                    self.status.showMessage("Error!")
                    return
                if values['lambda'] < 2 or values['mi'] < 2:
                    # TODO: Display error message  in place of result display.
                    self.status.showMessage("Error!")
                    return
                elif values['lambda'] < values['mi']:
                    # TODO: Display error message  in place of result display.
                    self.status.showMessage("Error!")
                    return

            self.run = True
            self.changed = False
            self.button.setText("&Stop!")
            if self.status:
                self.status.showMessage("Running!")
            self.start_simulation.emit(values)
            sleep(0.001)
        else:
            # Stop simulation without updating new parameters.
            self.run = False
            if not self.changed:
                self.button.setText("&Continue!")
                if self.status:
                    self.status.showMessage("Paused!")
            else:
                self.button.setText("&Run!")
                if self.status:
                    self.status.showMessage("Ready!")
            self.pause_simulation.emit()
            sleep(0.001)


    @QtCore.Slot()
    def finished(self):
        """
        Slot handling event of stopping simulation.
        """
        self.run = False
        self.changed = True
        self.button.setText("&Run!")
        if self.status:
            self.status.showMessage("Ready!")
        # TODO finalize process
