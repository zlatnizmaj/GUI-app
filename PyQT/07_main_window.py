# Filename: 07_main_window.py

"""Main Window-Style application."""
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QStatusBar, QToolBar

class Window(QMainWindow):
    """Main Windows."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("QMainWindow")
        self.setCentralWidget(QLabel("I'm the Central Widget"))
        self._createMenu()
        self._createToolBar()
        self._creatStatusBar()

    def _create