from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle


class Reporte_pagos(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1141, 802)


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

        self.lineEdit_cliente = QtWidgets.QLabel(self.centralwidget)
        self.lineEdit_cliente.setGeometry(QtCore.QRect(110, 280, 141, 31))
        self.lineEdit_cliente.setObjectName("lineEdit_cliente")

        self.lineEdit_monto = QtWidgets.QLabel(self.centralwidget)
        self.lineEdit_monto.setGeometry(QtCore.QRect(110, 360, 141, 31))
        self.lineEdit_monto.setObjectName("lineEdit_monto")

        self.lineEdit_metodo = QtWidgets.QLabel(self.centralwidget)
        self.lineEdit_metodo.setGeometry(QtCore.QRect(332, 360, 121, 31))
        self.lineEdit_metodo.setObjectName("lineEdit_metodo")

        self.lineEdit_fecha = QtWidgets.QLabel(self.centralwidget)
        self.lineEdit_fecha.setGeometry(QtCore.QRect(600, 260, 113, 21))
        self.lineEdit_fecha.setObjectName("lineEdit_fecha")

        self.comboBox_filtra = QtWidgets.QLabel(self.centralwidget)
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

        self.graphicsView = QtWidgets.QGraphicsView()
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


        
        self.pushButton.clicked.connect(self.consulta)


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



    def consulta (self):

        #--------------------------Comandos ORACLE--------------------------#

        #Conecta con BD
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()

        id_pago=self.lineEdit_filtra.text().strip()

        

        consulta_name= ('SELECT RAZ_SOC FROM PAGO JOIN CLIENTE USING(ID_CLI) WHERE ID_PAGO = {}'.format(id_pago))
        print(consulta_name)
        datos=cursor.execute(consulta_name).fetchall()

        tupla_cliente=[x[0]for x in datos]
        cliente=(tupla_cliente[0])

      
        self.lineEdit_cliente.setText(str(cliente.upper()))


        consulta_monto= ('SELECT MONTO FROM PAGO WHERE ID_PAGO = {}'.format(id_pago))
        datos1=cursor.execute(consulta_monto).fetchall()

        tupla_monto=[x[0]for x in datos1]
        monto=(tupla_monto[0])
        self.lineEdit_monto.setText(str(monto))


        consulta_metodo= ('SELECT METODO FROM PAGO JOIN METODO_PAGO USING(ID_MET)WHERE ID_PAGO = {}'.format(id_pago))
        datos2=cursor.execute(consulta_metodo).fetchall()

        tupla_metodo=[x[0]for x in datos2]
        metodo=(tupla_metodo[0])
        self.lineEdit_metodo.setText(str(metodo.upper()))

        print(str(cliente))
        print(monto)




        pass

    

    
