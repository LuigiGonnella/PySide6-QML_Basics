from PySide6.QtWidgets import QMainWindow, QPushButton, QSlider, QApplication
from PySide6.QtCore import Qt


class GoodSlider(QSlider):
    def __init__(self, value = 25, minimum = 0, maximum = 100):
        super().__init__(Qt.Orientation.Horizontal)
        self.setMaximum(maximum)
        self.setMinimum(minimum)
        self.setValue(value)
    
def respond_to_slider(new_value):
    print(f"Value changed: {new_value}")

app = QApplication()
slider = GoodSlider()

slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()


