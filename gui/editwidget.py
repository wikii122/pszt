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
        self.button = QtGui.QPushButton("Run!")

    def set_labels(self, labels):
        """
        Set label names in widget.
        """
        self.layout = QtGui.QFormLayout()
        for label in labels:
            edit = QtGui.QLineEdit()
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
