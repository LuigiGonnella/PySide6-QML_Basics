from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QBoxLayout

class RocWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RocWidget")

        self.button1 = QPushButton("Button1")
        self.button1.clicked.connect(self.button1_trigger)

        self.button2 = QPushButton("Button2")
        self.button2.clicked.connect(self.button2_trigger)

        self.buttons_layout = QVBoxLayout()
        self.buttons_layout.addWidget(self.button1)
        self.buttons_layout.addWidget(self.button2)
        print(self.buttons_layout.direction())
        self.buttons_layout.setDirection(QBoxLayout.Direction.BottomToTop)
        print(self.buttons_layout.direction())

        self.setLayout(self.buttons_layout)

    def button1_trigger(self):
        print("Button 1 clicked")

    def button2_trigger(self):
        print("Button 2 clicked")

