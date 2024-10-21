import functools
import random
from datetime import datetime

import pandas as pd
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtChart import QChart, QPieSeries, QPieSlice, QChartView, QBarCategoryAxis, QBarSet, QBarSeries, QValueAxis
from PyQt5.QtCore import Qt, QTimer, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor, QFont, QPainter
from PyQt5.QtWidgets import QTableWidgetItem, QLineEdit, QGridLayout, QComboBox
from PyQt5.uic.properties import QtGui

from database import head_list, list_info, filter_mine
from dateutil import parser
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class ComboBoxNEW(QtWidgets.QComboBox):
    popupAboutToBeShown = QtCore.pyqtSignal()

    def showPopup(self):
        self.popupAboutToBeShown.emit()
        super(ComboBoxNEW, self).showPopup()


class Ui_MainWindow(object):
    def __init__(self):
        self.chart = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1700, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1960, 900))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setTabsClosable(False)


        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.search_field = QLineEdit(self.tab_2)
        self.search_field.setStyleSheet('font-size: 19px; height: 30px;border-color:#004C99;border-width: 3px; border-style: solid;')
        self.search_field.setPlaceholderText("Qidiruv...")
        self.search_field.setGeometry(QtCore.QRect(83, 8, 600, 35))
        self.search_field.setObjectName("search_field")

        self.combo_box = QComboBox(self.tab_2)
        self.combo_box.setGeometry(700, 8, 180, 35)
        self.combo_box.setFont(QFont('Arial', 10))


        ###############list###############
        geek_list = ["all", "ohaktosh", "qum"]
        self.combo_box.addItems(geek_list)


        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(50, 50, 1800, 800))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(34)
        self.tableWidget.setRowCount(50)
        for i in range(0, len(head_list())):
            item = head_list()
            item = item[i]
            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(f"{item}"))

        ########table#########

        self.table_show(self.combo_box.currentText())
        self.combo_box.currentTextChanged.connect(self.table_show)
        self.combo_box.currentTextChanged.connect(self.second_create_bar)


        # self.tableWidget.itemChanged.connect(self.changed)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()




        self.search_field.textChanged.connect(self.search)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.analysis = QtWidgets.QPushButton(self.tab_2)
        self.analysis.setGeometry(QtCore.QRect(900, 8, 120, 35))
        self.analysis.setFont(QFont('Arial', 10))
        self.analysis.setStyleSheet("background-color : #004C99; color: white; font-style:bold")


        self.layoutdout = QGridLayout()
        self.tab_4.setLayout(self.layoutdout)


        # self.chartView3 = QChartView()
        # self.layoutdout.addWidget(self.chartView3)
        # self.second_create_bar()


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 888, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        # self.menuEdit = QtWidgets.QMenu(self.menubar)
        # self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_File = QtWidgets.QAction(MainWindow)
        self.actionAdd_File.setObjectName("actionAdd_File")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionAdd_File)
        self.menuFile.addAction(self.actionExit)
        # self.menuEdit.addAction(self.actionClear)
        # self.menuEdit.addAction(self.actionSelect_All)
        # self.menuEdit.addAction(self.actionLoad)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        # self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GeoMonitor"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "        Tablitsa        "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4),
                                  _translate("MainWindow", "        data        "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        # self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.analysis.setText(_translate("MainWindow", "Analiz"))
        self.actionAdd_File.setText(_translate("MainWindow", "Add File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def changed(self, item):
        import socket
        choice = QtWidgets.QMessageBox.question(self, ' Message ', "Are you sure Do you wanna change ?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            print(item.row(), item.column(), item.text())
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("192.168.1.3", 8080))
            print(s.getsockname()[0])
            s.close()
        else:
            pass


    def search(self, s):
        items = self.tableWidget.findItems(s, Qt.MatchContains)
        if items:
            item = items[0]
            self.tableWidget.setCurrentItem(item)


    def table_show(self, text):
        item = list_info()
        if text == 'all':
            for i in range(0, len(item)):
                for j in range(0, 34):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(f"{item[i][j]}"))
                    try:
                        dt_object = parser.parse(str(item[i][22]))
                        if (dt_object.date() - datetime.today().date()).days < 60:
                            self.tableWidget.item(i, j).setBackground(QColor(254, 168, 170))
                    except ValueError:
                        continue
                if item[i][7] == 'mavjud emas':
                    self.tableWidget.item(i, 7).setForeground(QColor(254, 4, 4))
                    self.tableWidget.item(i, 22).setForeground(QColor(254, 4, 4))
                    self.tableWidget.item(i, 7).setFont(QFont("Times", weight=QFont.Bold))
                    self.tableWidget.item(i, 22).setFont(QFont("Times", weight=QFont.Bold))
        else:
            self.tableWidget.removeRow(1)
            for j in range(0, 34):
                self.tableWidget.setItem(0, j, QTableWidgetItem(f"{item[0][j]}"))
                try:
                    dt_object = parser.parse(str(item[0][22]))
                    if (dt_object.date() - datetime.today().date()).days < 60:
                        self.tableWidget.item(0, j).setBackground(QColor(254, 168, 170))
                except ValueError:
                    continue
            if item[0][7] == 'mavjud emas':
                self.tableWidget.item(0, 7).setForeground(QColor(254, 4, 4))
                self.tableWidget.item(0, 22).setForeground(QColor(254, 4, 4))
                self.tableWidget.item(0, 7).setFont(QFont("Times", weight=QFont.Bold))
                self.tableWidget.item(0, 22).setFont(QFont("Times", weight=QFont.Bold))


    def second_create_bar(self):
        self.layoutdout.removeWidget(self.chart)
        list_inf = list_info()
        regions = ['Toshkent', 'Fargona', 'Jizzax', 'Sirdaryo', 'Xorazm', 'Namangan', 'Andijon', 'Samarqand', 'Buhoro',
                   'Qashqadaryo', "Qora Qolpog'iston"]

        # set1 = QBarSet('X1')
        # set2 = QBarSet('X2')
        # set3 = QBarSet('X3')
        # set4 = QBarSet('X4')
        series = QBarSeries()
        for i in range(11):
            set = QBarSet(regions[i])
            if regions[i] == 'Toshkent':
                if self.combo_box.currentText() == 'ohaktosh':
                    sum = int(list_inf[0][5])+int(list_inf[0][6])
                    set.append(sum)
                elif self.combo_box.currentText() == 'qum':
                    sum = int(list_inf[1][5]) + int(list_inf[1][6])
                    set.append(sum)
                elif self.combo_box.currentText() == 'all':
                    set.append(245)

            else:
                set.append(0)

            series.append(set)

        chart = QChart()
        chart.addSeries(series)

        chart.setTitle(str(self.combo_box.currentText()))
        chart.setAnimationOptions(QChart.SeriesAnimations)

        axisX = QBarCategoryAxis()
        for i in range(len(regions)):
            axisX.append(regions[i])

        axisY = QValueAxis()
        axisY.setRange(0, 200)


        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)
        chart.createDefaultAxes()
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        chartView = QChartView(chart)
        self.chart = chartView

        self.layoutdout.addWidget(chartView)

