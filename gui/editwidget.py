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

        self.layout = QtGui.QFormLayout()
        self.edits = list()

    def set_labels(self, labels):
        """
        Set label names in widget.
        """
        for label in labels:
            edit = QtGui.QLineEdit()
            self.layout.addRow(QtGui.QLabel(label), edit)
            self.edits.append(edit)

    def show(self):
        """
        Finalize layout and call QWidget.show() method.
        """
        self.setLayout(self.layout)
        super(EditWidget, self).show()
