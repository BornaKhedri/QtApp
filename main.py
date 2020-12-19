from qtTest import *
from appui import *

# def main():
#     app = QApplication(sys.argv)
#     win = MyWindow()
#     win.show()
#     sys.exit(app.exec_())


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
