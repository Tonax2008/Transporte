from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget ,QTableWidgetItem,QErrorMessage, QMessageBox
import cx_Oracle
class Viajes(object):

    #-------------------------------------------- Funcion MOVER entre Pantallas -----------------------------------------------------#

    def openwindow(self):

        #Define el objeto widget como una ventana principal
        self.window = QtWidgets.QMainWindow()
        #Define el objjeto ui , para regresar a la clase del script principal
        self.ui = Ui_Page2()
        #Manda un parametro a la ventana principal
        self.ui.setupUi(self.window)
        #Muestra la ventana 
        self.window.show()

    #-------------------------------------------------- Interfaz Buscar -----------------------------------------------------------#


    def setupUi(self, Form):
        


        #Crea  el tamaño de la ventana
        Form.setObjectName("Form")
        Form.resize(975, 709)

        #--------------------------------------------Contenedor Tabla de la BD-----------------------------------------------------#
       
        #Define las el contenedor de los widgets
        self.tableWidget = QtWidgets.QTableWidget(Form)
        #Establce el tamaño de los widgets
        self.tableWidget.setGeometry(QtCore.QRect(13, 56, 681, 441))
        self.tableWidget.setObjectName("tableWidget")
        #Columnas de la tabla (BD)
        self.tableWidget.setColumnCount(4)
        #Filas de la tabla (BD)
        self.tableWidget.setRowCount(20)

        # Titulo a cada columna
        self.tableWidget.setItem(0,0,QTableWidgetItem("ID VIAJE"))
        self.tableWidget.setItem(0,1,QTableWidgetItem("GASTO"))
        self.tableWidget.setItem(0,2,QTableWidgetItem("PRECIO"))
        self.tableWidget.setItem(0,3,QTableWidgetItem("DiSTANCIA"))
        self.tableWidget.setItem(0,4,QTableWidgetItem("DIRECCION"))
        
       #Conecta DB
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()


        consulta= ('select ID_VIA,GASTO,PRECIO,DISTANCIA FROM VIAJE')
        datos=cursor.execute(consulta).fetchall()
        

        #Consutlta direccion 
        adress=('SELECT CALLE , COLONIA,CP,DELEGACION,NO_INT,NO_EXT,ESTADO FROM VIAJE JOIN DIRECCION USING(ID_DIR) JOIN ESTADO USING (ID_EST) ')
        direccion= cursor.execute(adress).fetchall()

        #ciclo para recorrer tabla BD
        if len (datos) >0:
            fila =1
            for p in datos:
                columna=1
                for c in p:
                    celda=QTableWidgetItem(str(c))
                    self.tableWidget.setItem(fila,columna,celda)
                    columna +=1
                    fila +=1
        
        #Ciclo para rrecorer he imprimir dicrecciones BD

        if len (direccion) >0:
            fila=1

            for g in direccion:
                

                
                celda=QTableWidgetItem(str(g))
                self.tableWidget.setItem(fila,4,celda)
                    
                fila +=1

        #--------------------------------------------Boton Insertar-----------------------------------------------------#

        #Atributos del botn 
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        #Medidas del boton
        self.pushButton_3.setGeometry(QtCore.QRect(242, 12, 113, 32))
        #Nombre del objeto 
        self.pushButton_3.setObjectName("Insertar")

        #--------------------------------------------  Line Edit   -----------------------------------------------------#

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(369, 16, 221, 21))
        self.lineEdit.setObjectName("lineEdit")

        #--------------------------------------------   Boton Filtar -----------------------------------------------------#
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(12, 12, 113, 32))
        self.pushButton.setObjectName("pushButton")

        #-------------------------------------------- Boton Editar   -----------------------------------------------------#

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(127, 12, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        #--------------------------------------------  Boton Buscar  -----------------------------------------------------#

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(590, 10, 113, 32))
        self.pushButton_4.setObjectName("pushButton_4")

      

        #-----------------------------------------------  Textos  ----------------------------------------------------------#


        #Textos  de los botones que aparecen en la pantalla

        self.pushButton_3.setText( "Insertar")
        self.pushButton.setText  ( "Filtrar")
        self.pushButton_2.setText ("Editar")
        self.pushButton_4.setText ("Buscar")

  
        
        #Referencia a la ventana ?

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def retranslateUi(self, Page2):
        _translate = QtCore.QCoreApplication.translate
        #nombre ventana en la interfaz
        Page2.setWindowTitle(_translate("Page2", "Clientes"))


    #-------------------------------------------- Funcion Boton Regresar-----------------------------------------------------#

    def button_handler_back(self):
        self.openwindow()
