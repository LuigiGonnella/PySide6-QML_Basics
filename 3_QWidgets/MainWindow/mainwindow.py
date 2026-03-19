from PySide6.QtWidgets import QMainWindow, QToolBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction


class HomePage(QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app #useful to quit later
        self.setWindowTitle("Home Page")

        menu_bar = self.menuBar() #return a QMenuBar object

        #---------------FILE MENU -----------------------
        file_menu =  menu_bar.addMenu("File") #&File is a title, return a QMenu object
        quit_action = file_menu.addAction("Quit") #Return a QAction object

        quit_action.triggered.connect(self.quit_app) #QAction has the triggered signal, with parameter
        #checked=false by default
    
        #---------------EDIT MENU -----------------------
        edit_menu = menu_bar.addMenu("Edit")
        copy_action = edit_menu.addAction("Copy")
        cut_action = edit_menu.addAction("Cut")
        paste_action = edit_menu.addAction("Paste")
        undo_action = edit_menu.addAction("Undo")
        redo_action = edit_menu.addAction("Redo")

        
        #---------------SETTINGS MENU -----------------------
        settings_menu = menu_bar.addMenu("Settings")



        #---------------EXAMPLES MENU -----------------------
        examples_menu = menu_bar.addMenu("Examples")

        #---------------HELP MENU -----------------------
        help_menu = menu_bar.addMenu("Help")


        #--------------- TOOLBAR -----------------------
        toolbar = QToolBar("Tools & Utils")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar.addAction(quit_action) #same behaviour od quit from file menu


        #------------- ACTIONS ----------------
        action1 = QAction("Some Action", self) #self is parent here
        action1.setStatusTip("Status Message for this action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)




    def quit_app(self):
        self.app.quit()


    def toolbar_button_click(self):
        print("action 1 triggered")








