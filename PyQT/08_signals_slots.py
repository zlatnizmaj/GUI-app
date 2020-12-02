# Filename: 08_signals_slots

"""Signals and slots example."""
import sys
import functools

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

def greeting():
    """Slot function"""
    if msg.text():
        msg.setText("")
    else:
        msg.setText("Hello PyQT_Slots_Signals!!")

def greeting_who(who):
    """Slot function"""
    if msg.text():
        msg.setText("")
    else:
        msg.setText(f"Hello {who}")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Signals and slots")
layout = QVBoxLayout()

btn = QPushButton("Greet")
btn_who = QPushButton("Greet To You")
btn.clicked.connect(greeting)
btn_who.clicked.connect(functools.partial(greeting_who, "Nam Ng"))

layout.addWidget(btn)
layout.addWidget(btn_who)
msg = QLabel("")
layout.addWidget(msg)
window.setLayout(layout)

window.show()
sys.exit(app.exec())