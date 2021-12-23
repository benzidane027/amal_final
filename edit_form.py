# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main3.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form_edit(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.move(500,200)
        self.setFixedSize(230,405)
        self.setMaximumSize(QtCore.QSize(230, 350))
        self.setSizeIncrement(QtCore.QSize(230, 250))
        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 375, 81, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.erro_messsage=QtWidgets.QLabel(self)
        self.erro_messsage.move(10,350)
        self.erro_messsage.resize(200,20)


        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 10, 131, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_19 = QtWidgets.QLabel(self)
        self.label_19.setGeometry(QtCore.QRect(152, 10, 51, 20))
        self.label_19.setObjectName("label_19")
        self.lineEdit_7 = QtWidgets.QLineEdit(self)
        self.lineEdit_7.setGeometry(QtCore.QRect(33, 290, 161, 20))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_20 = QtWidgets.QLabel(self)
        self.label_20.setGeometry(QtCore.QRect(128, 50, 80, 19))
        self.label_20.setObjectName("label_20")
        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(112, 120, 91, 20))
        self.label_12.setObjectName("label_12")
        self.dateEdit = QtWidgets.QDateEdit(self)
        self.dateEdit.setGeometry(QtCore.QRect(25, 90, 100, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.comboBox_2 = QtWidgets.QComboBox(self)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 50, 101, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(31, 200, 172, 54))
        self.textEdit.setObjectName("textEdit")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(159, 170, 47, 31))
        self.label_7.setObjectName("label_7")
        self.label_22 = QtWidgets.QLabel(self)
        self.label_22.setGeometry(QtCore.QRect(143, 260, 61, 21))
        self.label_22.setObjectName("label_22")
        self.label_21 = QtWidgets.QLabel(self)
        self.label_21.setGeometry(QtCore.QRect(124, 90, 81, 20))
        self.label_21.setObjectName("label_21")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(32, 143, 171, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowTitle("تعديل شخص")
        self.pushButton_6.setText("تعديل")
        self.label_19.setText("الاسم")
        self.label_20.setText("مكان الولادة")
        self.label_12.setText("الرقم الوطني")
        self.comboBox_2.setItemText(0, "--------------")
        self.comboBox_2.setItemText(1,"دمشق")
        self.comboBox_2.setItemText(2, "ريف دمشق")
        self.comboBox_2.setItemText(3,  "حلب")
        self.comboBox_2.setItemText(4, "حماة")
        self.comboBox_2.setItemText(5, "اللاذقية")
        self.comboBox_2.setItemText(6, "طرطوس")
        self.comboBox_2.setItemText(7,  "درعا")
        self.comboBox_2.setItemText(8,  "الرقة")
        self.comboBox_2.setItemText(9, "دير الزور")
        self.comboBox_2.setItemText(10,  "ادلب")
        self.comboBox_2.setItemText(11,  "الحسكة ")
        self.comboBox_2.setItemText(12,  "القنيطرة")
        self.comboBox_2.setItemText(13,  "حمص")
        self.comboBox_2.setItemText(14,  "السويداء")
        self.label_7.setText( "العنوان")
        self.label_22.setText( "الاختصاص")
        self.label_21.setText("تاريخ الولادة")
    
if __name__ == '__main__':
    app =QtWidgets.QApplication(sys.argv)
  

    obj1=Ui_Form_edit()
    obj1.show()

    app.exec_()


