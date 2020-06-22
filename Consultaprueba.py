# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CONSULTA.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1049, 833)
        Form.setWindowTitle("")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(23, 130, 1001, 651))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.BT_INSERTAR = QtWidgets.QPushButton(Form)
        self.BT_INSERTAR.setGeometry(QtCore.QRect(242, 12, 113, 32))
        self.BT_INSERTAR.setObjectName("BT_INSERTAR")

        self.lineEdit_ELIMINAR = QtWidgets.QLineEdit(Form)
        self.lineEdit_ELIMINAR.setGeometry(QtCore.QRect(400, 20, 291, 21))
        self.lineEdit_ELIMINAR.setObjectName("lineEdit_ELIMINAR")

        self.BT_EDITAR = QtWidgets.QPushButton(Form)
        self.BT_EDITAR.setGeometry(QtCore.QRect(127, 12, 113, 32))
        self.BT_EDITAR.setObjectName("BT_EDITAR")

        self.BT_ELIMINAR = QtWidgets.QPushButton(Form)
        self.BT_ELIMINAR.setGeometry(QtCore.QRect(710, 10, 113, 32))
        self.BT_ELIMINAR.setObjectName("BT_ELIMINAR")

        self.BT_REGRESAR = QtWidgets.QPushButton(Form)
        self.BT_REGRESAR.setGeometry(QtCore.QRect(890, 10, 113, 32))
        self.BT_REGRESAR.setObjectName("BT_REGRESAR")
        self.BT_REGRESAR.clicked.connect(self.combo)

        self.CAMPO_1 = QtWidgets.QLabel(Form)
        self.CAMPO_1.setGeometry(QtCore.QRect(140, 60, 71, 16))
        self.CAMPO_1.setObjectName("CAMPO_1")

        self.CAMPO_2 = QtWidgets.QLabel(Form)
        self.CAMPO_2.setGeometry(QtCore.QRect(240, 60, 71, 16))
        self.CAMPO_2.setObjectName("CAMPO_2")

        self.CAMPO_3 = QtWidgets.QLabel(Form)
        self.CAMPO_3.setGeometry(QtCore.QRect(330, 60, 71, 16))
        self.CAMPO_3.setObjectName("CAMPO_3")

        self.CAMPO4 = QtWidgets.QLabel(Form)
        self.CAMPO4.setGeometry(QtCore.QRect(420, 60, 71, 16))
        self.CAMPO4.setObjectName("CAMPO4")

        self.CAMPO_5 = QtWidgets.QLabel(Form)
        self.CAMPO_5.setGeometry(QtCore.QRect(510, 60, 71, 16))
        self.CAMPO_5.setObjectName("CAMPO_5")

        self.CAMPO_6 = QtWidgets.QLabel(Form)
        self.CAMPO_6.setGeometry(QtCore.QRect(610, 60, 71, 16))
        self.CAMPO_6.setObjectName("CAMPO_6")

        self.CAMPO_7 = QtWidgets.QLabel(Form)
        self.CAMPO_7.setGeometry(QtCore.QRect(710, 60, 71, 16))
        self.CAMPO_7.setObjectName("CAMPO_7")

        self.CAMPO_8 = QtWidgets.QLabel(Form)
        self.CAMPO_8.setGeometry(QtCore.QRect(810, 60, 71, 16))
        self.CAMPO_8.setObjectName("CAMPO_8")

        self.lineEdit_C1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_C1.setGeometry(QtCore.QRect(130, 80, 81, 21))
        self.lineEdit_C1.setObjectName("lineEdit_C1")

        self.lineEdit_C2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_C2.setGeometry(QtCore.QRect(230, 80, 81, 21))
        self.lineEdit_C2.setObjectName("lineEdit_C2")

        self.lineEdit_C4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_C4.setGeometry(QtCore.QRect(410, 80, 81, 21))
        self.lineEdit_C4.setObjectName("lineEdit_C4")

        self.lineEdit_C3 =  QtWidgets.QComboBox(Form)
        self.lineEdit_C3.setGeometry(QtCore.QRect(320, 80, 81, 21))
        self.lineEdit_C3.setObjectName("lineEdit_C3")
        self.lineEdit_C3.addItem("")
        self.lineEdit_C3.addItem("")
        self.lineEdit_C3.addItem("cuwepo")

        self.lineEdit_C5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_C5.setGeometry(QtCore.QRect(510, 80, 81, 21))
        self.lineEdit_C5.setObjectName("lineEdit_C5")

        self.lineEdit_C7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_C7.setGeometry(QtCore.QRect(710, 80, 81, 21))
        self.lineEdit_C7.setObjectName("lineEdit_C7")

        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(810, 80, 81, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.lineEdit_C6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_C6.setGeometry(QtCore.QRect(610, 80, 81, 21))
        self.lineEdit_C6.setObjectName("lineEdit_C6")

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(30, 15, 71, 71))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        metodo= self.lineEdit_C3.currentIndex()
        print (metodo)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.BT_INSERTAR.setText(_translate("Form", "INSERTAR"))
        self.BT_EDITAR.setText(_translate("Form", "EDITAR"))
        self.BT_ELIMINAR.setText(_translate("Form", "ELIMINAR"))
        self.BT_REGRESAR.setText(_translate("Form", "REGRESAR"))
        self.CAMPO_1.setText(_translate("Form", "CAMPO1"))
        self.CAMPO_2.setText(_translate("Form", "CAMPO2"))
        self.CAMPO_3.setText(_translate("Form", "Metodo Pago"))
        self.CAMPO4.setText(_translate("Form", "CAMPO4"))
        self.CAMPO_5.setText(_translate("Form", "CAMPO5"))
        self.CAMPO_6.setText(_translate("Form", "CAMPO6"))
        self.CAMPO_7.setText(_translate("Form", "CAMPO 7"))
        self.CAMPO_8.setText(_translate("Form", "CAMPO 8"))


        self.comboBox.setItemText(0, _translate("Form", "FIL1"))
        self.comboBox.setItemText(1, _translate("Form", "FIL2"))
        self.comboBox.setItemText(2, _translate("Form", "FIL3"))

        self.lineEdit_C3.setItemText(0, _translate("Form", "Efectivo"))
        self.lineEdit_C3.setItemText(1, _translate("Form", "Cheque"))

    def combo (self):

        metodo= self.lineEdit_C3.currentIndex()
        print (metodo)

        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
