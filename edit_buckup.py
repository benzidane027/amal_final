# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main9.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_buckup(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(281, 271)
        self.move(500,200)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(10, 30, 261, 201))
        self.frame.setStyleSheet("border-color: rgb(136, 138, 133);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(130, 66, 121, 20))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(40, 20, 121, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(160, 23, 91, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(171, 143, 71, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 90, 161, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 180, 190, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(130, 120, 121, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 143, 161, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(80, 0, 121, 21))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 240, 91, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi()


    def retranslateUi(self):
        self.setWindowTitle("نسخ احتياطي" )
        self.label_3.setText(  "اختر اسم الملف :" )
        self.comboBox.setItemText(0,   "-----------------------" )
        self.comboBox.setItemText(1,   "اشخاص" )
        self.comboBox.setItemText(2,   "عائلات" )
        self.comboBox.setItemText(3,   "زيارات اطباء" )
        self.comboBox.setItemText(4,   "كفالات" )
        self.comboBox.setItemText(5,   "مواد" )
        self.comboBox.setItemText(6,   "المستودع" )
        self.label_2.setText(  "اختيار الجدول:" )
        self.pushButton_3.setText(  "folder.." )
        self.label_5.setText(  "اختر مكان الحفظ:" )
        self.label.setText(  "اخذ نسخة احتياطية" )
        self.pushButton_2.setText(  "حفظ" )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = Ui_Form_buckup()

    Form.show()
    sys.exit(app.exec_())
