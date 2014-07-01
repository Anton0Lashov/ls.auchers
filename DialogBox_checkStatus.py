# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogBox_checkStatus.ui'
#
# Created: Fri Jun 06 15:26:23 2014
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

class Ui_dialogBoxStatusCheck(object):
    def setupUi(self, dialogBoxStatusCheck):
        dialogBoxStatusCheck.setObjectName(_fromUtf8("dialogBoxStatusCheck"))
        dialogBoxStatusCheck.resize(280, 229)
        dialogBoxStatusCheck.setMinimumSize(QtCore.QSize(280, 229))
        dialogBoxStatusCheck.setMaximumSize(QtCore.QSize(280, 229))
        Ico = QtGui.QIcon()
        Ico.addPixmap(QtGui.QPixmap(_fromUtf8("ico/sm_ico.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        dialogBoxStatusCheck.setWindowIcon(Ico)
        self.centralwidget = QtGui.QWidget(dialogBoxStatusCheck)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.okBtn = QtGui.QPushButton(self.centralwidget)
        self.okBtn.setGeometry(QtCore.QRect(80, 180, 121, 23))
        self.okBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.okBtn.setObjectName(_fromUtf8("okBtn"))
        self.mainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.mainTextEdit.setGeometry(QtCore.QRect(0, 0, 281, 171))
        self.mainTextEdit.setReadOnly(True)
        self.mainTextEdit.setBackgroundVisible(False)
        self.mainTextEdit.setObjectName(_fromUtf8("mainTextEdit"))
        self.labelError = QtGui.QLabel(self.centralwidget)
        self.labelError.setEnabled(True)
        self.labelError.setGeometry(QtCore.QRect(10, 40, 261, 51))
        self.labelError.setAlignment(QtCore.Qt.AlignCenter)
        self.labelError.setObjectName(_fromUtf8("labelError"))
        dialogBoxStatusCheck.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(dialogBoxStatusCheck)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 280, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        dialogBoxStatusCheck.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(dialogBoxStatusCheck)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        dialogBoxStatusCheck.setStatusBar(self.statusbar)

        self.retranslateUi(dialogBoxStatusCheck)
        QtCore.QObject.connect(self.okBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), dialogBoxStatusCheck.close)
        QtCore.QMetaObject.connectSlotsByName(dialogBoxStatusCheck)

    def retranslateUi(self, dialogBoxStatusCheck):
        dialogBoxStatusCheck.setWindowTitle(_translate("dialogBoxStatusCheck", "Отчет о проверке", None))
        self.okBtn.setText(_translate("dialogBoxStatusCheck", "OK", None))
        self.labelError.setText(_translate("dialogBoxStatusCheck", "Проверка завершена с ошибками.", None))

