# Filename: 01_hello_pyqt.py

"""Simple Hello World example with PyQt5."""

# handle the exit status of the application
import sys
# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

# 2.Create an instance of QApplication.
app = QApplication(sys.argv)
# QApplication object also deals with common command line arguments, QApplication([]) empty list command line

# 3. Create an instance of your application's GUI
# QWidget, which is the base class of all user interface objects in PyQt.
window = QWidget()
window.setWindowTitle("PyQt5 App")
window.setGeometry(2500, 2500, 280, 80)
window.move(60, 15)
helloMsg = QLabel("<h1>Hello PyQt!<h1>", parent=window)
helloMsg.move(60, 15)

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec_())

'''
start the application’s event loop by calling app.exec_()
The call to .exec_() is wrapped in a call to sys.exit(), 
which allows you to cleanly exit Python and release memory resources when the application terminates
'''


