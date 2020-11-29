# Filename: 06_dialog.py

"""Dialog-Style application."""
import sys

from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QVBoxLayout

class Dialog(QDialog):
    """Dialog."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("QDialog")
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow("Name: ", QLineEdit())
        formLayout.addRow("Age: ", QLineEdit())
        formLayout.addRow("Job: ", QLineEdit())
        formLayout.addRow("Hobbies: ", QLineEdit())
        dlgLayout.addLayout(formLayout) # uses dlgLayout to arrange all the widgets on the form

        btns = QDialogButtonBox() # provides a convenient object to place the dialog buttons
        btns.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())