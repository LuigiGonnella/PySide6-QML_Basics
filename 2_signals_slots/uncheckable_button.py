from PySide6.QtWidgets import QApplication, QPushButton

#THE SLOT
def button_clicked():
    print("You clicked!! I got you!")

app = QApplication()
button = QPushButton("Press Me!") 
#checked=false as default

#CLICKED IS A SIGNAL OF THE QPushButton PARENT CLASS QAbstractButton
button.clicked.connect(button_clicked) #the connect() function i used to CONNECT a SIGNAL to a SLOT
button.show()
app.exec()
