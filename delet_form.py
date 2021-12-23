# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form_delet(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.move(500,300)
        self.setFixedSize(230, 130)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(80, 0, 81, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 190, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(70, 98, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi()
        self.lable_error=QtWidgets.QLabel(self)
        self.lable_error.setGeometry(QtCore.QRect(60, 70, 120, 25))
    
    def retranslateUi(self):
        
        #self.label.setText("حذف شخص")
        self.lineEdit.setPlaceholderText("ادخل رقم الشخص في الجدول")
        self.pushButton.setText("احذف")


