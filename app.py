from PyQt5.QtCore import QSize, Qt 
from PyQt5.QtWidgets import QApplication    #importing QApplication
from PyQt5.QtWidgets import QWidget         #importing QWidget
from PyQt5.QtWidgets import QPushButton     #importing QPushButton 
from PyQt5.QtWidgets import QMainWindow     #importing QMainWindow 
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit 
from PyQt5.QtWidgets import QVBoxLayout    
from random import choice
import sys  #used to access command line arguments

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.button_is_checked = True
        self.n_times_clicked = 0
        
        self.setWindowTitle("My App")   #naming the window
        
        self.label = QLabel()
        
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.button = QPushButton("Push")    #creating an instance of button
        self.button.setCheckable(False)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.the_window_title_changed)
        self.button.setChecked(self.button_is_checked)
        
        self.setCentralWidget(container)   #setting the central widget
        
        self.setFixedSize(QSize(400, 300))     #setting the window to be a fixed size

    def the_button_was_clicked(self):
        print("clicked")
        new_window_title = choice(window_titles)
        print("setting title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)
        
    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        
        print(self.button_is_checked)
        
    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        
        print(self.button_is_checked)
        
    def the_window_title_changed(self, window_title):
        print("window title changed: ", window_title)
         
        if window_title == "Something went wrong":
            self.button.setDisabled(True)

app = QApplication(sys.argv)    #only need one QApplication

window = MainWindow()   #setting the window to the main window class
window.show()           #showing the main window

app.exec_() #starts the event
