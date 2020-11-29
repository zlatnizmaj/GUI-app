import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
    # PyQT is initialized
    app = QApplication(sys.argv)
    widget = QWidget()

    # Text cannot be added immediately to a window. It has to be added to a label
    # A label is a widget that can show text or images
    textLabel = QLabel(widget)
    textLabel.setText("Hello PyQt!!!")
    textLabel.move(110, 85) # position (horizontal, vertical)

    widget.setGeometry(2500, 500, 320, 200) # starting position (50,50) and the window size (320,200)
    widget.setWindowTitle("PyQT5 Example")
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
