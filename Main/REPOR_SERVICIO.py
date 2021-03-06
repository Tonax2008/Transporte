from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle


class Reporte_Servicios (object):
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
        self.label_2.setGeometry(QtCore.QRect(90, 260, 80, 20))

        font = QtGui.QFont()
        font.setFamily("Apple Braille")
        font.setPointSize(17)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 360, 141, 20))

        font = QtGui.QFont()
        font.setFamily("Apple Braille")
        font.setPointSize(17)

        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 260, 81, 20))

        font = QtGui.QFont()
        font.setFamily("Apple Braille")
        font.setPointSize(17)

        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 260, 60, 16))

        font = QtGui.QFont()
        font.setFamily("Apple Braille")
        font.setPointSize(17)

        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(589, 260, 101, 20))

        font = QtGui.QFont()
        font.setFamily("Apple Braille")
        font.setPointSize(17)

        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(90, 300, 71, 16))
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(80, 400, 161, 16))
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(290, 320, 81, 16))
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(440, 320, 81, 16))
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(590, 330, 151, 16))
        self.label_12.setObjectName("label_12")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 1021, 22))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.pushButton.clicked.connect(self.Consulta)

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SERVICIO"))
        self.pushButton.setText(_translate("MainWindow", "BUSCAR"))
        self.label_2.setText(_translate("MainWindow", "CLIENTE"))
        self.label_3.setText(_translate("MainWindow", "DESCRIPCION"))
        self.label_4.setText(_translate("MainWindow", "MONTO"))
        self.label_5.setText(_translate("MainWindow", "UNIDAD"))
        self.label_6.setText(_translate("MainWindow", "EMPLEADO"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#808080;\">TextLabel</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#808080;\">TextLabel</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#808080;\">TextLabel</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#808080;\">TextLabel</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#808080;\">TextLabel</span></p></body></html>"))

    def Consulta (self):


        #Conecta BD
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()

        #Manda el valor de la caja de texto
        id_ser=self.lineEdit_filtra.text().strip()



        #AGREGAR COMOBOX PARA EVITAR BUSACR VARIOS ID

        consulta=("SELECT RAZ_SOC FROM SERVICIO JOIN CLIENTE USING (ID_CLI) WHERE ID_SER ={}".format(id_ser))
        datos=cursor.execute(consulta).fetchall()
        val_cliente=self.DATO_Tupla(datos.upper())
        #print(val_cliente)
        # self.label_8.setText(val_cliente)


        
        consuta_descr=("SELECT DESCRIPCION FROM SERVICIO WHERE ID_SER={}".format(id_ser))   #Realiza consutla a la BD
        dato_descr=cursor.execute(consuta_descr).fetchall()                                 #Ejecuta la consulta
        val_descr=self.DATO_Tupla(dato_descr)                                               #manda le valor a la funcion para convertir la tupla en texto
        self.label_9.setText(val_descr)                                                     #imprime elvalor en la etiqute
        #print(val_descr)
        

        consuta_Monto=("SELECT MONTO FROM SERVICIO JOIN PAGO USING (ID_PAGO) WHERE ID_SER={}".format(id_ser))
        dato_monto = cursor.execute(consuta_Monto).fetchall()
        val_monto=self.DATO_Tupla(dato_monto)
        self.label_10.setText(val_monto)

        consuta_uni=("SELECT PLACA FROM SERVICIO JOIN UNIDAD USING (ID_UNI) WHERE ID_SER={}".format(id_ser))
        dato_uni=cursor.execute(consuta_uni).fetchall()
        val_uni=self.DATO_Tupla(dato_uni)
        self.label_11.setText(val_uni)

        consulta_emp=("SELECT NOMBRE FROM SERVICIO JOIN EMPLEADO USING (ID_EMP) WHERE ID_SER={}".format(id_ser))
        dato_emp=cursor.execute(consulta_emp).fetchall()
        val_empl=self.DATO_Tupla(dato_emp)
        self.label_12.setText(val_empl.upper())

    
    def DATO_Tupla (self,dato):

        tupla=[x[0]for x in dato]
        valor=(tupla[0])
        #print(tupla)
        #print(valor)
        
        return (str(valor))

        