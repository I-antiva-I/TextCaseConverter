import sys

from PyQt5 import QtWidgets

from Control.MainController import MainController
from UI.MyWidgets.MyMainWindow import MyMainWindow


def launch():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyMainWindow()

    mainController = MainController(mainWindow)
    mainController.connectFunctions()

    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch()
