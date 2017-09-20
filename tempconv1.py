#!/usr/bin/python3

import sys, math
from PyQt5 import QtCore, uic, QtWidgets
 
# Cargar nuestro archivo .ui en misma carpeta de archivo.py 
form_class = uic.loadUiType("tempconv.ui")[0]
 
class MyWindowClass(QtWidgets.QMainWindow, form_class):
  def __init__(self, parent=None):
    QtWidgets.QMainWindow.__init__(self, parent)
    self.setupUi(self)
    self.btn_CtoF.clicked.connect(self.btn_CtoF_clicked)
    self.btn_FtoC.clicked.connect(self.btn_FtoC_clicked)

 # Evento del boton btn_CtoF
  def btn_CtoF_clicked(self):
      c = float(self.cel.text())
      f = round(( 9 / 5 ) * c + 32, 2)
      self.fah.setText(str(f))
 
 # Evento del boton btn_FtoC
  def btn_FtoC_clicked(self):
      f = float(self.fah.text())
      c = round((f - 32) * (5 / 9), 2)
      self.cel.setText(str(c))
 
app = QtWidgets.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()
