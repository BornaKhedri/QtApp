# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtSql import QSqlQueryModel, QSqlQuery, QSqlDatabase
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableView
import sqlite3 as LDBI
import pandas as pd
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


class Ui_MainWindow(QMainWindow):

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

        self.scene = QtWidgets.QGraphicsScene(self)
        self.figure = Figure()
        self.ax = self.figure.gca()
        self.ax.axes.xaxis.set_visible(False)
        self.ax.axes.yaxis.set_visible(False)
        canvas = FigureCanvas(self.figure)
        self.current_plot = ""
        canvas.setGeometry(0, 0, 755, 410)
        self.scene.addWidget(canvas)
        self.graphicsView.setScene(self.scene)

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
        self.menuView.addAction(self.actionList_Intersections)
        self.menuView.addAction(self.actionList_Streets)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionEnter_Full_Screen)
        self.menuHelp.addAction(self.actionAbout_the_App)
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        self.actionList_Intersections.setText(_translate("MainWindow", "List Intersections"))
        self.actionList_Streets.setText(_translate("MainWindow", "List Streets"))
        self.actionEnter_Full_Screen.setText(_translate("MainWindow", "Enter Full Screen"))
        self.actionAbout_the_App.setText(_translate("MainWindow", "About the App"))

        self.actionConnect.triggered.connect(self.conn_db)
        self.actionDisconnect.triggered.connect(self.disconn_db)
        self.actionAbout_the_App.triggered.connect(self.open_popup)
        self.actionList_Intersections.triggered.connect(self.intersections_popup)
        self.actionList_Streets.triggered.connect(self.streets_popup)
        self.actionEnter_Full_Screen.triggered.connect(self.full_screen)

        self.showStreet.stateChanged.connect(self.plot_checkboxes)
        self.showInt.stateChanged.connect(self.plot_checkboxes)
        self.showStName.stateChanged.connect(self.plot_checkboxes)

        self.toPNG.clicked.connect(lambda: self.save_to(type='png'))
        self.toPDF.clicked.connect(lambda: self.save_to(type='pdf'))


    def plot(self):
        self.fig_s, self.ax_s = plt.subplots()
        self.fig_i, self.ax_i = plt.subplots()
        self.fig_n, self.ax_n = plt.subplots()
        self.fig_si, self.ax_si = plt.subplots()
        self.fig_sn, self.ax_sn = plt.subplots()
        self.fig_in, self.ax_in = plt.subplots()
        self.fig_sin, self.ax_sin = plt.subplots()

        self.axes = [self.ax_s, self.ax_i, self.ax_n, self.ax_si, self.ax_sn, self.ax_in, self.ax_sin]
        for ax in self.axes:
            ax.set_xticks([])
            ax.set_yticks([])

        sd = 3  # size of the dots
        sx = 3  # size of the crosses
        f = 1.5  # fontsize

        x = self.Intersections.X.tolist()
        y = self.Intersections.Y.tolist()

        # create a new slope function:
        # https://stackoverflow.com/questions/41462419/python-slope-given-two-points-find-the-slope-answer-works-doesnt-work/41462583
        def slope(x1, y1, x2, y2):
            m = (y2 - y1) / (x2 - x1)
            return abs(m)

        # plot the roads
        for i in range(len(self.Roads)):
            index_0 = self.Roads.iloc[i].startNodeID
            index_1 = self.Roads.iloc[i].endNodeID

            x_values = [self.Intersections.iloc[index_0 - 1].X, self.Intersections.iloc[index_1 - 1].X]
            y_values = [self.Intersections.iloc[index_0 - 1].Y, self.Intersections.iloc[index_1 - 1].Y]
            self.ax_s.plot(x_values, y_values, linewidth=.5, color='deepskyblue')
            self.ax_si.plot(x_values, y_values, linewidth=.5, color='deepskyblue')
            self.ax_sn.plot(x_values, y_values, linewidth=.5, color='deepskyblue')
            self.ax_sin.plot(x_values, y_values, linewidth=.5, color='deepskyblue')

        # plot the labels
        for i in range(len(self.Roads)):
            index_0 = self.Roads.iloc[i].startNodeID
            index_1 = self.Roads.iloc[i].endNodeID
            x_value = (self.Intersections.iloc[index_0 - 1].X + self.Intersections.iloc[index_1 - 1].X) / 2
            y_value = (self.Intersections.iloc[index_0 - 1].Y + self.Intersections.iloc[index_1 - 1].Y) / 2

            m = slope(self.Intersections.iloc[index_0 - 1].X, self.Intersections.iloc[index_0 - 1].Y,
                      self.Intersections.iloc[index_1 - 1].X, self.Intersections.iloc[index_1 - 1].Y)

            if np.isclose(m, 0.3249197):
                rot = -13
                x_div = 8
                y_div = 1.5
            elif np.isclose(m, 3.0776835):
                rot = 66
                x_div = -4
                y_div = 1.5

            # self.ax_n.plot(x_values, y_values, linewidth=1, color='deepskyblue')
            self.ax_n.text(x_value + 0.024 / x_div, y_value + 0.008 / y_div, self.Roads.iloc[i]['name'], fontsize=f, rotation=rot,
                      rotation_mode='anchor', ha='center', va='center')
            self.ax_in.text(x_value + 0.024 / x_div, y_value + 0.008 / y_div, self.Roads.iloc[i]['name'], fontsize=f,
                       rotation=rot,
                       rotation_mode='anchor', ha='center', va='center')
            self.ax_sn.text(x_value + 0.024 / x_div, y_value + 0.008 / y_div, self.Roads.iloc[i]['name'], fontsize=f,
                       rotation=rot,
                       rotation_mode='anchor', ha='center', va='center')
            self.ax_sin.text(x_value + 0.024 / x_div, y_value + 0.008 / y_div, self.Roads.iloc[i]['name'], fontsize=f,
                        rotation=rot,
                        rotation_mode='anchor', ha='center', va='center')

        # plot red and green intersections
        l = []
        for index, row in self.InstalledFeatures.iterrows():
            if row.FeatureID == 1:
                marker = 'o'
                clr = 'red'
                msize = sd
            elif row.FeatureID == 2:
                marker = 'x'
                clr = 'green'
                msize = sx
            self.ax_i.plot(x[row.intersectionID - 1], y[row.intersectionID - 1], marker, color=clr, markersize=msize)
            l.append(row.intersectionID)
            self.ax_in.plot(x[row.intersectionID - 1], y[row.intersectionID - 1], marker, color=clr, markersize=msize)
            l.append(row.intersectionID)
            self.ax_si.plot(x[row.intersectionID - 1], y[row.intersectionID - 1], marker, color=clr, markersize=msize)
            l.append(row.intersectionID)
            self.ax_sin.plot(x[row.intersectionID - 1], y[row.intersectionID - 1], marker, color=clr, markersize=msize)
            l.append(row.intersectionID)

        # plot all other intersections
        not_ints = list(set(l))
        all_ints = self.Intersections.ID.tolist()
        ints = [x for x in all_ints if x not in not_ints]  # select the intersections thathave not been plotted yet
        for i in ints:
            self.ax_i.plot(x[i - 1], y[i - 1], 'o', color='black', markersize=sd)
            self.ax_in.plot(x[i - 1], y[i - 1], 'o', color='black', markersize=sd)
            self.ax_si.plot(x[i - 1], y[i - 1], 'o', color='black', markersize=sd)
            self.ax_sin.plot(x[i - 1], y[i - 1], 'o', color='black', markersize=sd)

    def plot_checkboxes(self):
        if 'db1' in dir(self):
            if self.showStreet.isChecked():
                if self.showInt.isChecked() and not self.showStName.isChecked():
                    canvas = FigureCanvas(self.fig_si)
                    self.current_plot = "fig_si"
                elif self.showStName.isChecked() and not self.showInt.isChecked():
                    canvas = FigureCanvas(self.fig_sn)
                    self.current_plot = "fig_sn"
                elif self.showInt.isChecked() and self.showStName.isChecked():
                    canvas = FigureCanvas(self.fig_sin)
                    self.current_plot = "fig_sin"
                else:
                    canvas = FigureCanvas(self.fig_s)
                    self.current_plot = "fig_s"

            if self.showInt.isChecked():
                if self.showStreet.isChecked() and not self.showStName.isChecked():
                    canvas = FigureCanvas(self.fig_si)
                    self.current_plot = "fig_si"
                elif self.showStName.isChecked() and not self.showStreet.isChecked():
                    canvas = FigureCanvas(self.fig_in)
                    self.current_plot = "fig_in"
                elif self.showStreet.isChecked() and self.showStName.isChecked():
                    canvas = FigureCanvas(self.fig_sin)
                    self.current_plot = "fig_sin"
                else:
                    canvas = FigureCanvas(self.fig_i)
                    self.current_plot = "fig_i"

            if self.showStName.isChecked():
                if self.showInt.isChecked() and not self.showStreet.isChecked():
                    canvas = FigureCanvas(self.fig_in)
                    self.current_plot = "fig_in"
                elif self.showStreet.isChecked() and not self.showInt.isChecked():
                    canvas = FigureCanvas(self.fig_sn)
                    self.current_plot = "fig_sn"
                elif self.showInt.isChecked() and self.showStreet.isChecked():
                    canvas = FigureCanvas(self.fig_sin)
                    self.current_plot = "fig_sin"
                else:
                    canvas = FigureCanvas(self.fig_n)
                    self.current_plot = "fig_n"

            if not self.showStreet.isChecked() and not self.showInt.isChecked() and not self.showStName.isChecked():
                canvas = FigureCanvas(self.figure)
                self.current_plot = ""

            print(self.current_plot)
            canvas.setGeometry(0, 0, 755, 410)
            self.scene.addWidget(canvas)
            self.graphicsView.setScene(self.scene)
        else:
            # print('There is no connected database')
            self.showStreet.setChecked(False)
            self.showInt.setChecked(False)
            self.showStName.setChecked(False)
            msg = QMessageBox()
            msg.setWindowTitle("Disconnection Error")
            txt = "There is no connected database"
            msg.setText(txt)
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def conn_db(self):
        if self.open_dialog_box() == 0:
            # print('No file selected / Selected file is not a database (only ".db" files)')
            msg = QMessageBox()
            msg.setWindowTitle("File Selection Error")
            txt = 'Either no file is selected or selected file is not a database (only ".db" files)'
            msg.setText(txt)
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.db1 = LDBI.connect(self.path)
            self.Roads = pd.read_sql_query("SELECT * from Roads", self.db1)
            self.Features = pd.read_sql_query("SELECT * from Features", self.db1)
            self.InstalledFeatures = pd.read_sql_query("SELECT * from InstalledFeatures", self.db1)
            self.Intersections = pd.read_sql_query("SELECT * from Intersections", self.db1)
            self.sqlite_sequence = pd.read_sql_query("SELECT * from sqlite_sequence", self.db1)
            self.plot()

            # print("Database connected")
            QMessageBox.about(self, 'Connected', 'Database connected.')

    def disconn_db(self):
        if 'db1' in dir(self):
            # print('Database disconnected')
            QMessageBox.about(self, 'Disconnected', 'Database disconnected.')
            del self.db1
            del self.fig_s, self.fig_i, self.fig_n, self.fig_si, self.fig_sn, self.fig_in, self.fig_sin

        else:
            # print('There is no connected database')
            msg = QMessageBox()
            msg.setWindowTitle("Disconnection Error")
            txt = "There is no connected database"
            msg.setText(txt)
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]
        if self.path[-3:] != '.db':
            return 0

    def save_to(self, type):
        option = QFileDialog.Options()
        if self.current_plot != "":
            if type == 'png':
                filename, _ = QFileDialog.getSaveFileName(self, "Export to PNG", self.current_plot + ".png",
                                                          "PNG Files (*.png);;All Files (*)", options=option)
            elif type == 'pdf':
                filename, _ = QFileDialog.getSaveFileName(self, "Export to PDF", self.current_plot + ".pdf",
                                                          "PDF Files (*.pdf);;All Files (*)", options=option)
            print(filename)
            if filename != "":
                plt = 'self.'+self.current_plot
                command = f"{plt}.savefig('{filename}', dpi=500)"
                exec(command)
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Saving Error")
                txt = "No file name was input"
                msg.setText(txt)
                msg.setIcon(QMessageBox.Critical)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Saving Error")
            txt = "There is no plot to export"
            msg.setText(txt)
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def open_popup(self):   # about the app popup
        msg = QMessageBox()
        msg.setWindowTitle("About IntersectionViewer (v1.0)")

        txt = ("This app is developed by Borna Arabkhedri. \n\n" +
        "From the 'Database' menu, you can connect to a database ('.db' format) " +
        "which has some data regarding roads, intersections, and installed features on those intersections. Then you " +
        "can use the checkbox buttons on the top of the map to select different layers to view the map. \n\n" +
        "Use the two buttons at the bottom of the page to export to PDF or PNG.")

        msg.setText(txt)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def open_sql_for_table_view(self):
        self.tableview = QTableView()
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.path)
        self.db.open()

    def intersections_popup(self):
        if 'db1' in dir(self):
            self.open_sql_for_table_view()

            sql_txt = """
            SELECT int.ID AS 'Intersection ID', int.X, int.Y, f.name AS 'Type of Feature'
            FROM Intersections AS int 
            LEFT JOIN InstalledFeatures AS inf ON int.ID = inf.intersectionID
            LEFT JOIN Features AS f ON inf.FeatureID = f.ID
            """

            query = QSqlQuery()
            query.exec(sql_txt)
            self.model = QSqlQueryModel()
            self.model.setQuery(query)
            self.tableview.setModel(self.model)
            self.tableview.show()
            self.db.close()
            return
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Database Error")
            txt = "There is no connected database"
            msg.setText(txt)
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return

    def streets_popup(self):
        if 'db1' in dir(self):
            self.open_sql_for_table_view()

            sql_txt = """
            SELECT R.name AS 'Road Name', R.ID AS 'Road ID', I1.X AS X1, I1.Y AS Y1, I2.X AS X2, I2.Y AS Y2
            FROM Roads as R, Intersections as I1, Intersections as I2 
            WHERE R.startNodeID = I1.ID 
            AND R.endNodeID = I2.ID 
            """

            query = QSqlQuery()
            query.exec(sql_txt)
            self.model = QSqlQueryModel()
            self.model.setQuery(query)
            self.tableview.setModel(self.model)
            self.tableview.show()
            self.db.close()
            return
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Database Error")
            txt = "There is no connected database"
            msg.setText(txt)
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return

    def full_screen(self):
        MainWindow = QtWidgets.QMainWindow()
        MainWindow.showMaximized()




    # def conn2_db(self):
    #     self.path = 'C:/Users/Borna/OneDrive/Quarter 4 - Au20/CESG 505 - Engineering Computing/Assignments/Final Project/App/Map.db'
    #     self.db1 = LDBI.connect(self.path)
    #     self.Roads = pd.read_sql_query("SELECT * from Roads", self.db1)
    #     self.Features = pd.read_sql_query("SELECT * from Features", self.db1)
    #     self.InstalledFeatures = pd.read_sql_query("SELECT * from InstalledFeatures", self.db1)
    #     self.Intersections = pd.read_sql_query("SELECT * from Intersections", self.db1)
    #     self.sqlite_sequence = pd.read_sql_query("SELECT * from sqlite_sequence", self.db1)




