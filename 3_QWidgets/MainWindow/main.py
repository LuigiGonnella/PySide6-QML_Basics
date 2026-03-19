from PySide6.QtWidgets import QApplication
from mainwindow import HomePage
import sys

app = QApplication(sys.argv)

window = HomePage(app)
window.show()

app.exec()