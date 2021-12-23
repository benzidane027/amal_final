# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main7.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_edit_meteriel(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(223, 295)
        self.move(500,200)
        self.label_29 = QtWidgets.QLabel(self)
        self.label_29.setGeometry(QtCore.QRect(130, 30, 71, 21))
        self.label_29.setObjectName("label_29")
        self.textEdit_5 = QtWidgets.QTextEdit(self)
        self.textEdit_5.setGeometry(QtCore.QRect(20, 120, 181, 101))
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_31 = QtWidgets.QLabel(self)
        self.label_31.setGeometry(QtCore.QRect(110, 100, 91, 20))
        self.label_31.setObjectName("label_31")
        self.label_30 = QtWidgets.QLabel(self)
        self.label_30.setGeometry(QtCore.QRect(150, 60, 47, 21))
        self.label_30.setObjectName("label_30")
        self.lineEdit_22 = QtWidgets.QLineEdit(self)
        self.lineEdit_22.setGeometry(QtCore.QRect(20, 30, 113, 20))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_52 = QtWidgets.QLineEdit(self)
        self.lineEdit_52.setGeometry(QtCore.QRect(20, 60, 113, 20))
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.pushButton_26 = QtWidgets.QPushButton(self)
        self.pushButton_26.setGeometry(QtCore.QRect(74, 265, 71, 25))
        self.pushButton_26.setObjectName("pushButton_26")
        self.label_140=QtWidgets.QLabel(self)
        self.label_140.move(40,235)
        self.label_140.resize(150,25)
 #       self.label_140.setText("تمت الاضافة بنجاح")
#        self.label_140.setText("قيمة خاطئة او حقل فارغ")

        self.retranslateUi()


    def retranslateUi(self):
        self.setWindowTitle("self")
        self.label_29.setText("رمز المادة")
        self.label_31.setText( "الملاحظات")
        self.label_30.setText("الوصف")
        self.pushButton_26.setText("تعديل")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    obj=Ui_Form_edit_meteriel()
    obj.show()
    sys.exit(app.exec_())
