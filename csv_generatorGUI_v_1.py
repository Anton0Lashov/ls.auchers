# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'csv_generatorGUI_v_1.ui'
#
# Created: Fri Jun 27 10:23:18 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(322, 297)
        MainWindow.setMinimumSize(QtCore.QSize(322, 170))
        MainWindow.setMaximumSize(QtCore.QSize(322, 297))
        icon = QtGui.QIcon('ico/sm_ico.png')
        ico_about = QtGui.QIcon()
        ico_about.addPixmap(QtGui.QPixmap(_fromUtf8("ico/about_ico.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.inputPath = QtGui.QLineEdit(self.centralwidget)
        self.inputPath.setGeometry(QtCore.QRect(10, 10, 181, 21))
        self.inputPath.setObjectName(_fromUtf8("inputPath"))
        self.selectIn = QtGui.QPushButton(self.centralwidget)
        self.selectIn.setGeometry(QtCore.QRect(200, 10, 111, 21))
        self.selectIn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selectIn.setObjectName(_fromUtf8("selectIn"))
        self.outputPath = QtGui.QLineEdit(self.centralwidget)
        self.outputPath.setGeometry(QtCore.QRect(6, 170, 181, 21))
        self.outputPath.setObjectName(_fromUtf8("outputPath"))
        self.saveAsBtn = QtGui.QPushButton(self.centralwidget)
        self.saveAsBtn.setGeometry(QtCore.QRect(196, 170, 111, 21))
        self.saveAsBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveAsBtn.setObjectName(_fromUtf8("saveAsBtn"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(6, 230, 301, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.param_label = QtGui.QLabel(self.centralwidget)
        self.param_label.setGeometry(QtCore.QRect(100, 40, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.param_label.setFont(font)
        self.param_label.setObjectName(_fromUtf8("param_label"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 60, 301, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_cp = QtGui.QLabel(self.centralwidget)
        self.label_cp.setGeometry(QtCore.QRect(110, 70, 111, 21))
        self.label_cp.setObjectName(_fromUtf8("label_cp"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(6, 150, 301, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.sm_rus = QtGui.QCheckBox(self.centralwidget)
        self.sm_rus.setGeometry(QtCore.QRect(20, 100, 70, 17))
        self.sm_rus.setObjectName(_fromUtf8("sm_rus"))
        self.sm_ua = QtGui.QCheckBox(self.centralwidget)
        self.sm_ua.setGeometry(QtCore.QRect(90, 100, 61, 17))
        self.sm_ua.setObjectName(_fromUtf8("sm_ua"))
        self.sm_kz = QtGui.QCheckBox(self.centralwidget)
        self.sm_kz.setGeometry(QtCore.QRect(160, 100, 61, 17))
        self.sm_kz.setObjectName(_fromUtf8("sm_kz"))
        self.sm_china = QtGui.QCheckBox(self.centralwidget)
        self.sm_china.setGeometry(QtCore.QRect(230, 100, 71, 17))
        self.sm_china.setObjectName(_fromUtf8("sm_china"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 200, 81, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.os_china = QtGui.QCheckBox(self.centralwidget)
        self.os_china.setGeometry(QtCore.QRect(230, 130, 71, 17))
        self.os_china.setObjectName(_fromUtf8("os_china"))
        self.os_rus = QtGui.QCheckBox(self.centralwidget)
        self.os_rus.setGeometry(QtCore.QRect(20, 130, 70, 17))
        self.os_rus.setObjectName(_fromUtf8("os_rus"))
        self.os_kz = QtGui.QCheckBox(self.centralwidget)
        self.os_kz.setGeometry(QtCore.QRect(160, 130, 61, 17))
        self.os_kz.setObjectName(_fromUtf8("os_kz"))
        self.os_ua = QtGui.QCheckBox(self.centralwidget)
        self.os_ua.setGeometry(QtCore.QRect(90, 130, 61, 17))
        self.os_ua.setObjectName(_fromUtf8("os_ua"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 322, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.helpMenu = QtGui.QMenu(self.menubar)
        self.helpMenu.setObjectName(_fromUtf8("helpMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.aboutApp = QtGui.QAction(MainWindow)
        self.aboutApp.setIcon(ico_about)
        self.aboutApp.setObjectName(_fromUtf8("aboutApp"))
        self.helpMenu.addAction(self.aboutApp)
        self.menubar.addAction(self.helpMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Club Pro Auchers Module", None))
        self.inputPath.setPlaceholderText(_translate("MainWindow", "Выберите файл Excel...", None))
        self.selectIn.setText(_translate("MainWindow", "Выберите файл", None))
        self.outputPath.setPlaceholderText(_translate("MainWindow", "Выберите путь для сохранения...", None))
        self.saveAsBtn.setText(_translate("MainWindow", "Сохранить как...", None))
        self.param_label.setText(_translate("MainWindow", "Выберите параметры", None))
        self.label_cp.setText(_translate("MainWindow", " Клубная программа", None))
        self.sm_rus.setText(_translate("MainWindow", "СМ РФ", None))
        self.sm_ua.setText(_translate("MainWindow", "СМ УФ", None))
        self.sm_kz.setText(_translate("MainWindow", "СМ КФ", None))
        self.sm_china.setText(_translate("MainWindow", "СМ Китай", None))
        self.pushButton.setText(_translate("MainWindow", "Выполнить", None))
        self.os_china.setText(_translate("MainWindow", "OS Китай", None))
        self.os_rus.setText(_translate("MainWindow", "OS РФ", None))
        self.os_kz.setText(_translate("MainWindow", "OS КФ", None))
        self.os_ua.setText(_translate("MainWindow", "OS УФ", None))
        self.helpMenu.setTitle(_translate("MainWindow", "Справка", None))
        self.aboutApp.setText(_translate("MainWindow", "О программе", None))

