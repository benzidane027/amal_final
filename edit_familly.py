# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main4.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_edit_familly(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("تعدبل عائلة")
        self.move(500,200)
        self.setFixedSize(242, 439)
        self.textEdit_6 = QtWidgets.QTextEdit(self)
        self.textEdit_6.setGeometry(QtCore.QRect(20, 325, 191, 41))
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_33 = QtWidgets.QLabel(self)
        self.label_33.setGeometry(QtCore.QRect(147, 110, 81, 20))
        self.label_33.setObjectName("label_33")
        self.textEdit_7 = QtWidgets.QTextEdit(self)
        self.textEdit_7.setGeometry(QtCore.QRect(20, 260, 191, 41))
        self.textEdit_7.setObjectName("textEdit_7")
        self.label_34 = QtWidgets.QLabel(self)
        self.label_34.setGeometry(QtCore.QRect(117, 180, 111, 20))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self)
        self.label_35.setGeometry(QtCore.QRect(80, 302, 141, 21))
        self.label_35.setObjectName("label_35")
        self.label_37 = QtWidgets.QLabel(self)
        self.label_37.setGeometry(QtCore.QRect(157, 20, 71, 20))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self)
        self.label_38.setGeometry(QtCore.QRect(90, 240, 141, 20))
        self.label_38.setObjectName("label_38")
        self.lineEdit_26 = QtWidgets.QLineEdit(self)
        self.lineEdit_26.setGeometry(QtCore.QRect(16, 83, 111, 20))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_27 = QtWidgets.QLineEdit(self)
        self.lineEdit_27.setGeometry(QtCore.QRect(16, 110, 121, 20))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(16, 21, 131, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_39 = QtWidgets.QLabel(self)
        self.label_39.setGeometry(QtCore.QRect(84, 130, 111, 20))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self)
        self.label_40.setGeometry(QtCore.QRect(157, 50, 71, 20))
        self.label_40.setObjectName("label_40")
        self.lineEdit_28 = QtWidgets.QLineEdit(self)
        self.lineEdit_28.setGeometry(QtCore.QRect(20, 220, 111, 20))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_29 = QtWidgets.QLineEdit(self)
        self.lineEdit_29.setGeometry(QtCore.QRect(16, 150, 191, 20))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.label_45 = QtWidgets.QLabel(self)
        self.label_45.setGeometry(QtCore.QRect(147, 80, 81, 20))
        self.label_45.setObjectName("label_45")
        self.spinBox_3 = QtWidgets.QSpinBox(self)
        self.spinBox_3.setGeometry(QtCore.QRect(20, 180, 81, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.lineEdit_30 = QtWidgets.QLineEdit(self)
        self.lineEdit_30.setGeometry(QtCore.QRect(16, 51, 121, 20))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.label_46 = QtWidgets.QLabel(self)
        self.label_46.setGeometry(QtCore.QRect(157, 214, 71, 20))
        self.label_46.setObjectName("label_46")
        self.label_143 = QtWidgets.QLabel(self)
        self.label_143.setGeometry(QtCore.QRect(30, 380, 151, 21))
        self.label_143.setObjectName("label_143")
        self.pushButton_29 = QtWidgets.QPushButton(self)
        self.pushButton_29.setGeometry(QtCore.QRect(70, 405, 91, 25))
        self.pushButton_29.setObjectName("pushButton_29")

        self.retranslateUi()

    def retranslateUi(self):
        self.label_33.setText("رقم الموبايل")
        self.label_34.setText("عدد افراد العائلة ")
        self.label_35.setText("مكان السكن السابق")
        self.label_37.setText("اسم الزوج")
        self.label_38.setText("مكان السكن الحالي")
        self.label_39.setText("رقم دفتر العائلة")
        self.label_40.setText("اسم الزوجة")
        self.label_45.setText("الرقم الوطني")
        self.label_46.setText("عمل الزوج")
        self.pushButton_29.setText("تعديل")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = Ui_Form_edit_familly()

    Form.show()
    sys.exit(app.exec_())
