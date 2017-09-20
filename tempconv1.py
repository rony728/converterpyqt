#!/usr/bin/python3
# -*- coding: utf-8 -*-
 

 
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
  cel = float(self.editCel.text())
  fahr = cel * 9 / 5.0 + 32
  self.spinFahr.setValue(int(fahr + 0.5))
 
 # Evento del boton btn_FtoC
 def btn_FtoC_clicked(self):
  fahr = self.spinFahr.value()
  cel = ((fahr - 32) * 5) / 9
  self.editCel.setText(str(cel))
 
app = QtWidgets.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()