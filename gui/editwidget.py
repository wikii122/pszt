"""
Widget used to handle edit fields.
"""
from PySide import QtGui


class EditWidget(QtGui.QWidget):
    """
    Widget used for handling input.
    """
    def __init__(self, *args, **kwarg):
        super(EditWidget, self).__init__(*args, **kwarg)
        self.main_layout = QtGui.QVBoxLayout()
        self.edits = list()
        self.button = QtGui.QPushButton("Run!", self)
        self.button.clicked.connect(self.push_button)
        self.labels = None

    def set_labels(self, labels):
        """
        Set label names in widget.
        """
        self.layout = QtGui.QFormLayout()
        self.labels = labels
        for label in labels:
            edit = QtGui.QLineEdit()
            edit.setValidator(QtGui.QIntValidator(edit))
            self.layout.addRow(QtGui.QLabel(label), edit)
            self.edits.append(edit)

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

        edits = map(lambda x: x.text(), self.edits)
        values = {x:y for x, y in zip(self.labels, edits)}
        # TODO make this more subtle.
        for x in values:
            if not values[x]:
                QtGui.QMessageBox.question(self, 'Message', "Empty field!")
                break
        # TODO correct input handling.
