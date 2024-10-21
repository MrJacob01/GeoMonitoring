import os
import os.path
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDesktopWidget
import aboutgui
import licensemain
import anaxcel


class abouthandel(QtWidgets.QMainWindow, aboutgui.Ui_MainWindow):


    def __init__(self, parent=None):
        super(abouthandel, self).__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(open("Dark/darkstyle.qss", "r").read())
        self.setWindowFlags(self.windowFlags() | Qt.Popup | Qt.WindowStaysOnTopHint)
        self.center()


    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()
        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())