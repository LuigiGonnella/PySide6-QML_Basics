from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from push_button import PushButton
import sys

app = QApplication(sys.argv)

window = PushButton() #hidden by default
window.show() #we show it


#Start event loop
app.exec()