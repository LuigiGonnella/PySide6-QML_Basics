from PySide6.QtWidgets import QMainWindow, QPushButton

class PushButton(QMainWindow):
    def __init__(self, text=None):
        super().__init__()

        self.setWindowTitle("Button Holder App")

        if text is None:
            self.button = QPushButton("Press Me!")
        else:
            self.button = QPushButton(text)
            
        self.setCentralWidget(self.button)