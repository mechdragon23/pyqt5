from PyQt5.QtCore import QSize, Qt 
from PyQt5.QtWidgets import QApplication    #importing QApplication
from PyQt5.QtWidgets import QWidget         #importing QWidget
from PyQt5.QtWidgets import QPushButton     #importing QPushButton 
from PyQt5.QtWidgets import QMainWindow     #importing QMainWindow 
import sys  #used to access command line arguments

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")   #naming the window
        
        button = QPushButton("Push")    #creating an instance of button
        
        self.setCentralWidget(button)   #setting the central widget
        
        self.setFixedSize(QSize(400, 300))     #setting the window to be a fixed size

app = QApplication(sys.argv)    #only need one QApplication

window = MainWindow()   #setting the window to the main window class
window.show()           #showing the main window

app.exec_() #starts the event
