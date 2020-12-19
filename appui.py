# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
import sqlite3 as LDBI
import pandas as pd
import matplotlib.pyplot as plt


class Ui_MainWindow(QMainWindow):
    # def __init__(self):
    #     super(Ui_MainWindow, self).__init__()
    #     self.setupUi()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 640)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.plotOpt = QtWidgets.QLabel(self.frame)
        self.plotOpt.setGeometry(QtCore.QRect(20, 10, 81, 31))
        self.plotOpt.setObjectName("plotOpt")

        self.showStreet = QtWidgets.QCheckBox(self.frame)
        self.showStreet.setGeometry(QtCore.QRect(200, 9, 111, 31))
        self.showStreet.setObjectName("showStreet")

        self.showInt = QtWidgets.QCheckBox(self.frame)
        self.showInt.setGeometry(QtCore.QRect(390, 10, 141, 31))
        self.showInt.setObjectName("showInt")

        self.showStName = QtWidgets.QCheckBox(self.frame)
        self.showStName.setGeometry(QtCore.QRect(600, 10, 141, 31))
        self.showStName.setObjectName("showStName")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(15, 61, 761, 431))
        self.graphicsView.setObjectName("graphicsView")

        self.toPDF = QtWidgets.QPushButton(self.centralwidget)
        self.toPDF.setGeometry(QtCore.QRect(20, 520, 361, 41))
        self.toPDF.setObjectName("toPDF")

        self.toPNG = QtWidgets.QPushButton(self.centralwidget)
        self.toPNG.setGeometry(QtCore.QRect(410, 520, 361, 41))
        self.toPNG.setObjectName("toPNG")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 26))
        self.menubar.setObjectName("menubar")

        self.menuDatabase = QtWidgets.QMenu(self.menubar)
        self.menuDatabase.setObjectName("menuDatabase")

        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")

        self.actionDisconnect = QtWidgets.QAction(MainWindow)
        self.actionDisconnect.setObjectName("actionDisconnect")

        self.actionShow_Tab_Bar = QtWidgets.QAction(MainWindow)
        self.actionShow_Tab_Bar.setObjectName("actionShow_Tab_Bar")

        self.actionShow_All_Tabs = QtWidgets.QAction(MainWindow)
        self.actionShow_All_Tabs.setObjectName("actionShow_All_Tabs")

        self.actionList_Intersections = QtWidgets.QAction(MainWindow)
        self.actionList_Intersections.setObjectName("actionList_Intersections")

        self.actionList_Streets = QtWidgets.QAction(MainWindow)
        self.actionList_Streets.setObjectName("actionList_Streets")

        self.actionEnter_Full_Screen = QtWidgets.QAction(MainWindow)
        self.actionEnter_Full_Screen.setObjectName("actionEnter_Full_Screen")

        self.actionAbout_the_App = QtWidgets.QAction(MainWindow)
        self.actionAbout_the_App.setObjectName("actionAbout_the_App")

        self.menuDatabase.addAction(self.actionConnect)
        self.menuDatabase.addAction(self.actionDisconnect)
        self.menuView.addAction(self.actionShow_Tab_Bar)
        self.menuView.addAction(self.actionShow_All_Tabs)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionList_Intersections)
        self.menuView.addAction(self.actionList_Streets)
        self.menuView.addAction(self.actionEnter_Full_Screen)
        self.menuHelp.addAction(self.actionAbout_the_App)
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def plot(self):
        data = []
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IntersectionViewer (v1.0)"))
        self.plotOpt.setText(_translate("MainWindow", "Plot Options:"))
        self.showStreet.setText(_translate("MainWindow", "Show Streets"))
        self.showInt.setText(_translate("MainWindow", "Show Intersections"))
        self.showStName.setText(_translate("MainWindow", "Show Street Names"))
        self.toPDF.setText(_translate("MainWindow", "Export to PDF"))
        self.toPNG.setText(_translate("MainWindow", "Export to PNG"))
        self.menuDatabase.setTitle(_translate("MainWindow", "Database"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.actionShow_Tab_Bar.setText(_translate("MainWindow", "Show Tab Bar"))
        self.actionShow_All_Tabs.setText(_translate("MainWindow", "Show All Tabs"))
        self.actionList_Intersections.setText(_translate("MainWindow", "List Intersections"))
        self.actionList_Streets.setText(_translate("MainWindow", "List Streets"))
        self.actionEnter_Full_Screen.setText(_translate("MainWindow", "Enter Full Screen"))
        self.actionAbout_the_App.setText(_translate("MainWindow", "About the App"))

        self.actionConnect.triggered.connect(self.conn_db)
        self.actionDisconnect.triggered.connect(self.disconn_db)
        self.actionAbout_the_App.triggered.connect(self.open_popup)

    def conn_db(self):
        if self.open_dialog_box() == 0:
            print('No file selected / Selected file is not a database (only ".db" files)')
        else:
            self.db1 = LDBI.connect(self.path)

            self.Roads = pd.read_sql_query("SELECT * from Roads", self.db1)
            self.Features = pd.read_sql_query("SELECT * from Features", self.db1)
            self.InstalledFeatures = pd.read_sql_query("SELECT * from InstalledFeatures", self.db1)
            self.Intersections = pd.read_sql_query("SELECT * from Intersections", self.db1)
            self.sqlite_sequence = pd.read_sql_query("SELECT * from sqlite_sequence", self.db1)

            print("Database connected")

    def disconn_db(self):
        if 'db1' in dir(self):
            print('Database disconnected')
            del self.db1
        else:
            print('There is no connected database')

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]
        if self.path[-3:] != '.db':
            return 0

    def open_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("About IntersectionViewer (v1.0)")

        txt = ("This app is developed by Borna Arabkhedri. \n\n" +
        "From the 'Database' menu, you can connect to a database ('.db' format) " +
        "which has data regarding roads, intersections, and installed features on those intersections. Then you " +
        "can use the checkbox buttons on the top of the map to select different layers to view the map. \n\n" +
        "Use the two buttons at the bottom of the page to export to PDF or PNG.")

        msg.setText(txt)
        x = msg.exec_()


