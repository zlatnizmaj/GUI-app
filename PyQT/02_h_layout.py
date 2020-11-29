# Filename: 02_h_layout.py

"""Horizontal layout example.
QHBoxLayout classes
"""
import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QHBoxLayout")
layout = QHBoxLayout() # creates a QHBoxLayout object called layout
layout.addWidget(QPushButton('Left')) # add three buttons to layout with .addWidget()
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Right'))
window.setLayout(layout) # sets layout as your window’s layout with .setLayout()

window.show()
sys.exit(app.exec_())