
from UI.MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    mainWindow = Ui_MainWindow()
    mainWindow.setupUi(window)
    mainWindow.setupSignals()
    window.show()
    sys.exit(app.exec_())