from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle


class Reporte_pagos(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 711)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 40, 321, 91))

        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(36)

        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setObjectName("label")

        self.lineEdit_cliente = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cliente.setGeometry(QtCore.QRect(110, 280, 141, 31))
        self.lineEdit_cliente.setObjectName("lineEdit_cliente")

        self.lineEdit_monto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_monto.setGeometry(QtCore.QRect(110, 360, 141, 31))
        self.lineEdit_monto.setObjectName("lineEdit_monto")

        self.lineEdit_metodo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_metodo.setGeometry(QtCore.QRect(332, 360, 121, 31))
        self.lineEdit_metodo.setObjectName("lineEdit_metodo")

        self.lineEdit_fecha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_fecha.setGeometry(QtCore.QRect(600, 260, 113, 21))
        self.lineEdit_fecha.setObjectName("lineEdit_fecha")

        self.comboBox_filtra = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_filtra.setGeometry(QtCore.QRect(100, 160, 91, 31))
        self.comboBox_filtra.setObjectName("comboBox_filtra")

        self.lineEdit_filtra = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_filtra.setGeometry(QtCore.QRect(360, 160, 191, 21))
        self.lineEdit_filtra.setObjectName("lineEdit_filtra")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(560, 160, 91, 32))
        self.pushButton.setObjectName("pushButton")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(129, 250, 81, 20))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 330, 81, 20))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 330, 81, 20))
        self.label_4.setObjectName("label_4")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(240, 430, 491, 192))
        self.graphicsView.setObjectName("graphicsView")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1021, 22))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")


        #CONSULTA BD

           #--------------------------Comandos ORACLE--------------------------#
         #Conecta con BD
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()

        consulta= ('SELECT RAZ_SOC,MONTO,METODO,FECHA FROM PAGO  JOIN CLIENTE USING (ID_CLI) JOIN METODO_PAGO USING (ID_MET) ')
        datos=cursor.execute(consulta).fetchall()
        

        #------------CONSULTAS-------------#
        #ciclo para recorrer tabla BD
        if len (datos) >0:
            fila =1
            for p in datos:
                columna=0
                for c in p:
                    celda=QTableWidgetItem(str(c))
                    self.tableWidget.setItem(fila,columna,celda)
                    columna +=1
                fila +=1
        





        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "PAGOS"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label_2.setText(_translate("MainWindow", "CLIENTE"))
        self.label_3.setText(_translate("MainWindow", "MONTO"))
        self.label_4.setText(_translate("MainWindow", "METODO"))
