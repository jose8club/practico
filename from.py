#!/usr/bin/python
# ­*­ coding: utf­8 ­*­
# Nombre archivo: view_form.py
import sys
from PySide import QtGui, QtCore

#Importamos el constructor de la clase generada automáticamente
from hola import Ui_Dialog
class Form(QtGui.QDialog):

    def __init__(self, parent=None, trigger=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui =  Ui_Dialog()
        self.ui.setupUi(self)
        """self.ui.ok.clicked.connect(self.ok)
        self.setModal(True)"""
        self.show()

    def cancel(self):
        self.reject()

    def ok(self):
        self.accept()
        
    	


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = Form()
    sys.exit(app.exec_())



