import sys

from PyQt4 import QtCore, QtGui
QtCore.Signal = QtCore.pyqtSignal
from .ui.mainwindow import Ui_MainWindow

class Main(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Do any other initiation, connect UI signals to functions, etc.
