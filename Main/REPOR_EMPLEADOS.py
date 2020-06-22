from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle

class Reporte_Empleados(object):
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
        self.label_2.setGeometry(QtCore.QRect(90, 250, 80, 20))
        font = QtGui.QFont()

        font.setFamily("Apple Braille")
        font.setPointSize(17)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 250, 141, 20))
        
        font = QtGui.QFont()
        font.setFamily("Apple Braille")
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 250, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Apple Braille")
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)

        self.label_5.setGeometry(QtCore.QRect(480, 250, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Apple Braille")
        font.setPointSize(17)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        
        self.label_6.setGeometry(QtCore.QRect(589, 250, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Apple Braille")
        font.setPointSize(17)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(730, 250, 111, 16))

        font = QtGui.QFont()
        font.setFamily("Apple Braille")
        font.setPointSize(17)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(90, 340, 71, 16))
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(179, 340, 161, 16))
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(360, 340, 81, 16))
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(480, 340, 110, 16))
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(600, 340, 60, 16))
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(709, 340, 371, 71))
        self.label_13.setObjectName("label_13")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1021, 22))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #CONSULTA BD

        self.pushButton.clicked.connect(self.consulta)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "EMPLEADOS"))
        self.pushButton.setText(_translate("MainWindow", "BUSCAR"))
        self.label_2.setText(_translate("MainWindow", "Nombre"))
        self.label_3.setText(_translate("MainWindow", "APELLIDOS"))
        self.label_4.setText(_translate("MainWindow", "Telefono"))
        self.label_5.setText(_translate("MainWindow", "CORREO"))
        self.label_6.setText(_translate("MainWindow", "NO. SEGURO"))
        self.label_7.setText(_translate("MainWindow", "DIRECCION"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#808080;\">TextLabel</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#808080;\">TextLabel</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#808080;\">TextLabel</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#808080;\">TextLabel</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#808080;\">TextLabel</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#808080;\">TextLabel</span></p></body></html>"))

    def consulta (self):

        #Conecta con la BD
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()

        id_emp=self.lineEdit_filtra.text().strip()


        #Consutla 
        #consulta= ('SELECT NOMBRE, APE_PAT ,APE_MAT ,TELEFONO,CORREO,NO_SEG FROM EMPLEADO JOIN CORREO USING (ID_COR) ')
        consulta_name=('SELECT NOMBRE FROM EMPLEADO WHERE ID_EMP ={}'.format(id_emp))
        
        datos=cursor.execute(consulta_name).fetchall()

        tupla_name=[x[0]for x in datos]
        name=(tupla_name[0])
        self.label_8.setText(str(name))


        consulta_ape=('SELECT APE_PAT ,APE_MAT FROM EMPLEADO WHERE ID_EMP= {}'.format(id_emp))
        dato_ape=cursor.execute(consulta_ape).fetchall()
        
        tupla_ape=[x for x in dato_ape]
        print(tupla_ape)
        ape=(tupla_ape[0])
        print(ape)
        
        self.label_9.setText(str(ape))

        consulta_tel=("SELECT TELEFONO FROM EMPLEADO WHERE ID_EMP={}".format(id_emp))
        print(consulta_tel)
        dato_tel=cursor.execute(consulta_tel).fetchall()
        tupla_tel=[x[0]for x in dato_tel]
        tel=(tupla_tel[0])
        self.label_10.setText(str(tel))

        consulta_correo=('SELECT CORREO FROM EMPLEADO JOIN CORREO USING (ID_COR) WHERE ID_EMP={}'.format(id_emp))
        dato_correo=cursor.execute(consulta_correo).fetchall()
        tupla_correo=[x[0]for x in dato_correo]
        correo=(tupla_correo[0])
        self.label_11.setText(str(correo))

        consulta_seguro=('SELECT NO_SEG FROM EMPLEADO WHERE ID_EMP={}'.format(id_emp))
        dato_seguro=cursor.execute(consulta_seguro).fetchall()
        tupla_seguro=[x[0]for x in dato_seguro]
        seguro=(tupla_seguro[0])
        self.label_12.setText(str(seguro))
        
        #Consutlta direccion 
        adress=('SELECT CALLE , COLONIA,CP,DELEGACION,NO_INT,NO_EXT,ESTADO FROM EMPLEaDO JOIN DIRECCION USING(ID_DIR) JOIN ESTADO USING (ID_EST) where ID_EMP={}'.format(id_emp))
        direccion= cursor.execute(adress).fetchall()
    
        tupla_direccion=[x[0]for x in direccion]
        direc=(tupla_direccion[0])

        print(direccion)
        self.label_13.setText(str(direccion))
        
