# Filename: pycalc.py

"""PyCalc is a simple calculator built using Python and PyQt5."""
import sys
# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QVBoxLayout

__version__ = "0.1"
__author__ = "Nam Ng"

# Create a subclass of QMainWindow to setup the calculator's GUI
class PyCalcUi(QMainWindow): # creates the GUI with the class PyCalcUi, inherits from QMainWindow
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer"""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle("PyCalc")
        self.setFixedSize(235, 235) # user won’t be able to resize the window

        # Set the central widget and the general layout
        self._centralWidget = QWidget(self) # since your GUI class inherits from QMainWindow, you need a central widget
        # This object will be the parent for the rest of the GUI component
        self.setCentralWidget(self._centralWidget)
        self.generalLayout = QVBoxLayout()
        self._centralWidget.setLayout(self.generalLayout)

        # Create the display and the buttons
        self._createDisplay()
        self._createButtons()
        """use a QVBoxLayout to place the display at the top and the buttons in a grid layout at the bottom"""
    # Snip
    def _createDisplay(self):
        """Create the display"""
        # Create the display widget

# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = PyCalcUi()
    view.show()
    # Execute the calculator's main loop
    sys.exit(pycalc.exec()) # runs the application’s event loop with pycalc.exec()

if __name__ == '__main__':
    main()