# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main6.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_edit_spons(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(214, 315)
        self.move(500,200)
        self.label_26 = QtWidgets.QLabel(self)
        self.label_26.setGeometry(QtCore.QRect(100, 201, 81, 20))
        self.label_26.setObjectName("label_26")
        self.label_16 = QtWidgets.QLabel(self)
        self.label_16.setGeometry(QtCore.QRect(110, 11, 71, 20))
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self)
        self.label_18.setGeometry(QtCore.QRect(70, 93, 111, 20))
        self.label_18.setObjectName("label_18")
        self.comboBox_6 = QtWidgets.QComboBox(self)
        self.comboBox_6.setGeometry(QtCore.QRect(30, 30, 111, 25))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_8 = QtWidgets.QComboBox(self)
        self.comboBox_8.setGeometry(QtCore.QRect(20, 70, 111, 25))
        self.comboBox_8.setObjectName("comboBox_8")
        self.dateEdit_3 = QtWidgets.QDateEdit(self)
        self.dateEdit_3.setGeometry(QtCore.QRect(20, 115, 110, 22))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.label_24 = QtWidgets.QLabel(self)
        self.label_24.setGeometry(QtCore.QRect(70, 140, 111, 20))
        self.label_24.setObjectName("label_24")
        self.dateEdit_4 = QtWidgets.QDateEdit(self)
        self.dateEdit_4.setGeometry(QtCore.QRect(20, 162, 110, 22))
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.comboBox_3 = QtWidgets.QComboBox(self)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 201, 91, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.label_17 = QtWidgets.QLabel(self)
        self.label_17.setGeometry(QtCore.QRect(90, 50, 91, 20))
        self.label_17.setObjectName("label_17")
        self.pushButton_23 = QtWidgets.QPushButton(self)
        self.pushButton_23.setGeometry(QtCore.QRect(70, 280, 71, 25))
        self.pushButton_23.setObjectName("pushButton_23")
        self.label_139 = QtWidgets.QLabel(self)
        self.label_139.setGeometry(QtCore.QRect(30, 240, 161, 21))
        self.label_139.setText("")
        self.label_139.setObjectName("label_139")

        self.retranslateUi()


    def retranslateUi(self):

        self.setWindowTitle("Form")
        self.label_26.setText("نوع الكفالة")
        self.label_16.setText("اسم الكفيل")
        self.label_18.setText("تاريخ ببدء الكفالة")
        self.label_24.setText("تاريخ انتهاء الكفالة")
        self.comboBox_3.setItemText(0, "------------------")
        self.label_17.setText("اسم المستفيد")
        self.pushButton_23.setText("تعديل")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    obj=Ui_Form_edit_spons()
    obj.show()
    sys.exit(app.exec_())
