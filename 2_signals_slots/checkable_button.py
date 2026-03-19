from PySide6.QtWidgets import QApplication, QPushButton

#THE SLOT
def button_clicked(data):
    print("You clicked!! I got you!")
    print(f"State: {data}") #True = checked
                            #False = unchecked

app = QApplication()
button = QPushButton("Press Me!") 
#checked=false as default
button.setCheckable(True) #now button is a checkbox 

#CLICKED IS A SIGNAL OF THE QPushButton PARENT CLASS QAbstractButton
button.clicked.connect(button_clicked) #the connect() function i used to CONNECT a SIGNAL to a SLOT
button.show()
app.exec()
