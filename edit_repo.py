# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main8.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3,datetime

class Ui_Form_edit_repo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.db=sqlite3.connect("amal.db")
        self.cr=self.db.cursor()
        self.setWindowTitle("تعديل")
        self.setFixedSize(321, 350)
        self.move(500,200)
        self.label_42 = QtWidgets.QLabel(self)
        self.label_42.setGeometry(QtCore.QRect(220, 220, 81, 20))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self)
        self.label_43.setGeometry(QtCore.QRect(20, 220, 81, 20))
        self.label_43.setObjectName("label_43")
        self.lineEdit_54 = QtWidgets.QLineEdit(self)
        self.lineEdit_54.setEnabled(True)
        self.lineEdit_54.setGeometry(QtCore.QRect(113, 120, 91, 20))
        self.lineEdit_54.setObjectName("lineEdit_54")
        self.label_44 = QtWidgets.QLabel(self)
        self.label_44.setGeometry(QtCore.QRect(70, 10, 91, 31))
        self.label_44.setObjectName("label_44")
        self.lineEdit_53 = QtWidgets.QLineEdit(self)
        self.lineEdit_53.setEnabled(True)
        self.lineEdit_53.setGeometry(QtCore.QRect(10, 120, 91, 20))
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.label_32 = QtWidgets.QLabel(self)
        self.label_32.setGeometry(QtCore.QRect(124, 220, 71, 20))
        self.label_32.setObjectName("label_32")
        self.lineEdit_55 = QtWidgets.QLineEdit(self)
        self.lineEdit_55.setEnabled(True)
        self.lineEdit_55.setGeometry(QtCore.QRect(113, 150, 91, 20))
        self.lineEdit_55.setObjectName("lineEdit_55")
        self.comboBox_7 = QtWidgets.QComboBox(self)
        self.comboBox_7.setGeometry(QtCore.QRect(30, 250, 69, 22))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.lineEdit_42 = QtWidgets.QLineEdit(self)
        self.lineEdit_42.setEnabled(True)
        self.lineEdit_42.setGeometry(QtCore.QRect(10, 180, 91, 20))
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.lineEdit_50 = QtWidgets.QLineEdit(self)
        self.lineEdit_50.setEnabled(True)
        self.lineEdit_50.setGeometry(QtCore.QRect(10, 150, 91, 20))
        self.lineEdit_50.setObjectName("lineEdit_50")
        self.label_36 = QtWidgets.QLabel(self)
        self.label_36.setGeometry(QtCore.QRect(220, 20, 81, 20))
        self.label_36.setObjectName("label_36")
        self.lineEdit_57 = QtWidgets.QLineEdit(self)
        self.lineEdit_57.setEnabled(True)
        self.lineEdit_57.setGeometry(QtCore.QRect(210, 120, 91, 20))
        self.lineEdit_57.setObjectName("lineEdit_57")
        self.spinBox_2 = QtWidgets.QSpinBox(self)
        self.spinBox_2.setGeometry(QtCore.QRect(130, 250, 48, 26))
        self.spinBox_2.setObjectName("spinBox_2")
        self.lineEdit_40 = QtWidgets.QLineEdit(self)
        self.lineEdit_40.setEnabled(True)
        self.lineEdit_40.setGeometry(QtCore.QRect(210, 180, 91, 20))
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.lineEdit_41 = QtWidgets.QLineEdit(self)
        self.lineEdit_41.setEnabled(True)
        self.lineEdit_41.setGeometry(QtCore.QRect(113, 180, 91, 20))
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.comboBox_5 = QtWidgets.QComboBox(self)
        self.comboBox_5.setGeometry(QtCore.QRect(210, 50, 91, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.dateEdit_6 = QtWidgets.QDateEdit(self)
        self.dateEdit_6.setGeometry(QtCore.QRect(194, 250, 110, 22))
        self.dateEdit_6.setObjectName("dateEdit_6")
        self.dateEdit_6.setDisplayFormat("yyyy/MM/dd")
        self.comboBox_20 = QtWidgets.QComboBox(self)
        self.comboBox_20.setGeometry(QtCore.QRect(24, 50, 141, 22))
        self.comboBox_20.setObjectName("comboBox_20")
        self.comboBox_20.addItem("")
        self.lineEdit_56 = QtWidgets.QLineEdit(self)
        self.lineEdit_56.setEnabled(True)
        self.lineEdit_56.setGeometry(QtCore.QRect(210, 150, 91, 20))
        self.lineEdit_56.setObjectName("lineEdit_56")
        self.pushButton_34 = QtWidgets.QPushButton(self)
        self.pushButton_34.setGeometry(QtCore.QRect(120, 320, 91, 25))
        self.pushButton_34.setObjectName("pushButton_34")
        self.label_141 = QtWidgets.QLabel(self)
        self.label_141.setGeometry(QtCore.QRect(60, 290, 211, 21))
        self.label_141.setText("")
        self.label_141.setObjectName("label_141")
        self.label_41 = QtWidgets.QLabel(self)
        self.label_41.setGeometry(QtCore.QRect(250, 90, 51, 20))
        self.label_41.setObjectName("label_41")
        
        self.retranslateUi()
        #******************* myCode
        self.spinBox_2.valueChanged.connect(self.hide_lineEdit)
        self.comboBox_5.currentIndexChanged.connect(self.inset_info_inCb)
    def set_(self,id):
        self.insert_info(id)
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_42.setText("تاريخ العملية")
        self.label_43.setText("نوع العملية")
        self.label_44.setText("الاسم و الرقم")
        self.label_32.setText("عدد المواد")
        self.comboBox_7.setItemText(0, "------------")
        self.comboBox_7.setItemText(1, "ادخال ")
        self.comboBox_7.setItemText(2, "اخراج")
        self.label_36.setText("التسليم من ")
        self.comboBox_5.setItemText(0, "-------------------")
        self.comboBox_5.setItemText(1, "موظفين")
        self.comboBox_5.setItemText(2, "كفلاء")
        self.comboBox_5.setItemText(3, "مستفيدين")
        self.comboBox_20.setItemText(0, "--------------------------------")
        self.pushButton_34.setText("تعديل")
        self.label_41.setText("المواد")
    def hide_lineEdit(self,value):
        list_=[self.lineEdit_57,self.lineEdit_54,self.lineEdit_53,self.lineEdit_56,self.lineEdit_55,self.lineEdit_50,self.lineEdit_40,self.lineEdit_41,self.lineEdit_42]
        if self.spinBox_2.value()==0:
            self.spinBox_2.setValue(1)
        elif self.spinBox_2.value()>9:
            self.spinBox_2.setValue(9)
        for i in range(self.spinBox_2.value()):
            list_[i].setEnabled(True)
        for i in range(self.spinBox_2.value(),9):
            list_[i].setEnabled(False)
            list_[i].clear()        
    def inset_info_inCb(self):
        
        if self.comboBox_5.currentIndex()==0:
            self.comboBox_20.clear()
            self.comboBox_20.addItem("--------------------------------")

        elif self.comboBox_5.currentIndex()==1:
            self.comboBox_20.clear()
            self.comboBox_20.addItem("--------------------------------")
            tp="موظفين"
            record=self.cr.execute(f"select name,national_number from person where type_of_peson='{tp}';").fetchall()
            #print(record)
            for item in record:
                self.comboBox_20.addItem(item[0]+" "+item[1])
        elif self.comboBox_5.currentIndex()==2:
            self.comboBox_20.clear()
            self.comboBox_20.addItem("--------------------------------")
            tp="كفلاء"
            record=self.cr.execute(f"select name,national_number from person where type_of_peson='{tp}';").fetchall()
            #print(record)
            for item in record:
                self.comboBox_20.addItem(item[0]+" "+item[1])
        elif self.comboBox_5.currentIndex()==3:
            self.comboBox_20.clear()
            self.comboBox_20.addItem("--------------------------------")
            tp="مستفيدين"
            record=self.cr.execute(f"select name,national_number from person where type_of_peson='{tp}';").fetchall()
            #print(record)
            for item in record:
                self.comboBox_20.addItem(item[0]+" "+item[1])
    def insert_info(self,id):
        list_=[self.lineEdit_57,self.lineEdit_54,self.lineEdit_53,self.lineEdit_56,self.lineEdit_55,self.lineEdit_50,self.lineEdit_40,self.lineEdit_41,self.lineEdit_42]

        record=self.cr.execute(f"select * from repo where id='{id}'").fetchall()
        self.comboBox_5.setCurrentText(record[0][1])
        self.comboBox_20.setCurrentText(record[0][2])
        self.comboBox_7.setCurrentText(record[0][5])
        self.dateEdit_6.setDate(datetime.datetime.strptime(str(record[0][3]).replace("/","-"), '%Y-%m-%d').date())
        self.spinBox_2.setValue(int(record[0][4]))
        for i,item in enumerate(list_):
            if item.isEnabled():
                item.setText(record[0][i+6])






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    obj=Ui_Form_edit_repo()
    obj.set_(14)
    obj.show()

    sys.exit(app.exec_())
