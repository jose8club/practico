# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hola.ui'
#
# Created: Thu Jun  6 11:41:21 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label1 = QtGui.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(30, 10, 331, 111))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label1.setFont(font)
        self.label1.setTextFormat(QtCore.Qt.PlainText)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.label2 = QtGui.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(30, 120, 341, 131))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label1.setText(QtGui.QApplication.translate("Dialog", "Hola GitHub ", None, QtGui.QApplication.UnicodeUTF8))
        self.label2.setText(QtGui.QApplication.translate("Dialog", "Soy José Luis", None, QtGui.QApplication.UnicodeUTF8))

