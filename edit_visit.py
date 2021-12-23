# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main5.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_edit_visit(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("self")
        self.setFixedSize(229, 346)
        self.move(500,200)
        self.textEdit_4 = QtWidgets.QTextEdit(self)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 200, 181, 71))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_14 = QtWidgets.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(140, 39, 61, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(110, 90, 91, 20))
        self.label_15.setObjectName("label_15")
        self.label_23 = QtWidgets.QLabel(self)
        self.label_23.setGeometry(QtCore.QRect(110, 130, 91, 20))
        self.label_23.setObjectName("label_23")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(22, 24, 111, 25))
        self.comboBox.setObjectName("comboBox")
        self.dateEdit_2 = QtWidgets.QDateEdit(self)
        self.dateEdit_2.setGeometry(QtCore.QRect(20, 150, 110, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_33 = QtWidgets.QLabel(self)
        self.label_33.setGeometry(QtCore.QRect(24, 65, 131, 24))
        self.label_33.setStyleSheet("border:1px solid rgb(186, 189, 182);\n"
"background-color: rgb(243, 243, 243);")
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(120, 5, 85, 20))
        self.label_13.setObjectName("label_13")
        self.comboBox_4 = QtWidgets.QComboBox(self)
        self.comboBox_4.setGeometry(QtCore.QRect(25, 110, 111, 25))
        self.comboBox_4.setObjectName("comboBox_4")
        self.pushButton_17 = QtWidgets.QPushButton(self)
        self.pushButton_17.setGeometry(QtCore.QRect(94, 315, 51, 25))
        self.pushButton_17.setObjectName("pushButton_17")
        self.label_138 = QtWidgets.QLabel(self)
        self.label_138.setGeometry(QtCore.QRect(41, 280, 151, 21))
        self.label_138.setText("")
        self.label_138.setObjectName("label_138")
        self.label_00=QtWidgets.QLabel(self)
        self.label_00.setText("التشخيص")
        self.label_00.move(150,180)

        self.retranslateUi()


    def retranslateUi(self):


        self.label_14.setText("الاختصاص")
        self.label_15.setText("اسم المستفيد")
        self.label_23.setText("تاريخ المعاينة")
        self.label_13.setText("اسم  الطبيب")
        self.pushButton_17.setText("تعديل")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    obj=Ui_Form_edit_visit()
    obj.show()
    sys.exit(app.exec_())
