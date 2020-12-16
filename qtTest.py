from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from tkinter import *

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.screenWidth = Tk().winfo_screenwidth()
        self.screenHeight = Tk().winfo_screenheight()
        self.appWidth = 500
        self.appHeight = 300
        self.setGeometry(int(self.screenWidth / 2 - self.appWidth / 2), int(self.screenHeight / 2 - self.appHeight / 2),
                         self.appWidth, self.appHeight)
        self.setWindowTitle("Borna's Template")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("First Label!")
        self.label.move(int(self.appWidth/2), int(self.appHeight/2))

        self.b = QtWidgets.QPushButton(self)
        self.b.setText("Click Me")
        self.b.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()
