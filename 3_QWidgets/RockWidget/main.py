from PySide6.QtWidgets import QWidget, QApplication, QMainWindow
import sys
from rockwidget import RocWidget

app = QApplication(sys.argv)

main_window = QMainWindow()
roc_widget = RocWidget()


roc_widget.show()
app.exec()