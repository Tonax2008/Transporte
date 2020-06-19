from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget ,QTableWidgetItem,QErrorMessage, QMessageBox
import cx_Oracle
import VENPRIN

class PAGOS (object):


     #-------------------------------------------- Funcion MOVER entre Pantallas -----------------------------------------------------#

    def openwindow(self):

        #Define el objeto widget como una ventana principal
        self.window = QtWidgets.QMainWindow()
        #Define el objjeto ui , para regresar a la clase del script principal
        self.ui = VENPRIN.Ui_Page2()
        #Manda un parametro a la ventana principal
        self.ui.setupUi(self.window)
        #Muestra la ventana 
        self.window.show()
    #-------------------------------------------------- FUNCION Interfaz CONSULTA -----------------------------------------------------------#

    def setupUi(self, Form):

        self.mensajes= QMessageBox()

        #------------------------------------VENTANA PRINCIPAL------------------------------------------#
        #define una venata
        Form.setObjectName("Form")
        #Dedine tamaño de la ventana principal
        Form.resize(1049, 833)
        #Nombre de la ventana 
        Form.setWindowTitle("Pagos")


        #------------------------------------TABLA CONTENODR BD------------------------------------------# 
        
        #define la tabla
        self.tableWidget = QtWidgets.QTableWidget(Form)
        #Size de la tabla cordenadas (L,R,U,D)
        self.tableWidget.setGeometry(QtCore.QRect(23, 130, 1001, 651))
        #Nombre de la tablas
        self.tableWidget.setObjectName("tableWidget")
        #Columnas de la tabla
        self.tableWidget.setColumnCount(5)
        #fila de la tabla
        self.tableWidget.setRowCount(25)

        # Titulo a cada celda
        self.tableWidget.setItem(0,0,QTableWidgetItem("ID_PAGO"))
        self.tableWidget.setItem(0,1,QTableWidgetItem("FECHA"))
        self.tableWidget.setItem(0,2,QTableWidgetItem("ID METODO"))
        self.tableWidget.setItem(0,3,QTableWidgetItem("MONTO"))
        self.tableWidget.setItem(0,4,QTableWidgetItem("ID CLIENTE"))


        #--------------------------Comandos ORACLE--------------------------#
         #Conecta con BD
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()

        consulta= ('SELECT ID_PAGO ,FECHA ,ID_MET,MONTO,ID_CLI FROM PAGO')
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
        
       

        #------------------------------------ BOTONES -----------------------------------------#

        #---Boton insertar---#
        
        #Declara un boton
        self.BT_INSERTAR = QtWidgets.QPushButton(Form)
        #Size boton
        self.BT_INSERTAR.setGeometry(QtCore.QRect(242, 12, 113, 32))
        #Nombre del objeto 
        self.BT_INSERTAR.setObjectName("BT_INSERTAR")
        #Conecta el botn con la funcion insertar 
        self.BT_INSERTAR.clicked.connect(self.insertar)


    #---Boton Editar---#

        self.BT_EDITAR = QtWidgets.QPushButton(Form)
        self.BT_EDITAR.setGeometry(QtCore.QRect(127, 12, 113, 32))
        self.BT_EDITAR.setObjectName("BT_EDITAR")

        #---Boton ELIMINAR---#

        self.BT_ELIMINAR = QtWidgets.QPushButton(Form)
        self.BT_ELIMINAR.setGeometry(QtCore.QRect(710, 10, 113, 32))
        self.BT_ELIMINAR.setObjectName("BT_ELIMINAR")

        #---Boton Regresar---#

        self.BT_REGRESAR = QtWidgets.QPushButton(Form)
        self.BT_REGRESAR.setGeometry(QtCore.QRect(890, 10, 113, 32))
        self.BT_REGRESAR.setObjectName("BT_REGRESAR")

       

        #------------------------------------ ETIQUETAS -----------------------------------------#

        #declara un obejto label
        self.CAMPO_1 = QtWidgets.QLabel(Form)
        #Size de la etiqueta
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


       

        
        #------------------------------------ Text Edit (barra de texto editable) -----------------------------------------#

        #---cuadro de ELIMINAR--#
        # Declara un text edit 
        self.lineEdit_ELIMINAR = QtWidgets.QLineEdit(Form)
        #Size text edit
        self.lineEdit_ELIMINAR.setGeometry(QtCore.QRect(400, 20, 291, 21))
        self.lineEdit_ELIMINAR.setObjectName("lineEdit_ELIMINAR")

        #---cuadro de nombre--#
        self.lineEdit_C1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_C1.setGeometry(QtCore.QRect(130, 80, 81, 21))
        self.lineEdit_C1.setObjectName("lineEdit_C1")


        self.lineEdit_C2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_C2.setGeometry(QtCore.QRect(230, 80, 81, 21))
        self.lineEdit_C2.setObjectName("lineEdit_C2")




        self.lineEdit_C3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_C3.setGeometry(QtCore.QRect(320, 80, 81, 21))
        self.lineEdit_C3.setObjectName("lineEdit_C3")

        self.lineEdit_C4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_C4.setGeometry(QtCore.QRect(410, 80, 81, 21))
        self.lineEdit_C4.setObjectName("lineEdit_C4")



        self.lineEdit_C5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_C5.setGeometry(QtCore.QRect(510, 80, 81, 21))
        self.lineEdit_C5.setObjectName("lineEdit_C5")


        

        #---------------------- Caja de filtrar  con sus opciones-------------#
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(30, 15, 71, 71))
        self.comboBox.setObjectName("comboBox")
        #texto de las listas a seleccionar
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        
        #textos de los botones y campos
        self.BT_INSERTAR.setText( "INSERTAR")
        self.BT_EDITAR.setText( "EDITAR")
        self.BT_ELIMINAR.setText( "ELIMINAR")
        self.BT_REGRESAR.setText( "REGRESAR")
        self.CAMPO_1.setText( "ID_PAGO")
        self.CAMPO_2.setText( "FECHA")
        self.CAMPO_3.setText( "METODO")
        self.CAMPO4.setText( "MONTO")
        self.CAMPO_5.setText( "CLIENTE")
        
        self.comboBox.setItemText(0,  "FIL1")
        self.comboBox.setItemText(1,  "FIL2")
        self.comboBox.setItemText(2,  "FIL3")

    def insertar(self):


        valor_id=self.lineEdit_C1.text().strip()
        fecha=self.lineEdit_C2.text().strip()
        bus_met=self.lineEdit_C3.text().strip()
        monto=self.lineEdit_C4.text().strip()
        bus_clie=self.lineEdit_C5.text().strip()

        
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()


        busqueda_1=("Select id_met from metodo_pago  where METODO= '{}'".format(bus_met))
        resultado_1=cursor.execute(busqueda_1).fetchall()

        busqueda_2=("Select id_cli from cliente  where RAZ_SOC= '{}'".format(bus_clie))
        resultado_2=cursor.execute(busqueda_2).fetchall()

        #print(resultado_1)
        metod=[x[0] for x in resultado_1]
        #print(metod)
        t_metod=(metod[0])
        #print(m_metod)

        cliente=[x[0]for x in resultado_2]
        t_cliente=(cliente[0])


       
        
        idmet=int(t_metod)
        #print(idmet)        
        cliente_id=t_cliente


       



        if not self.exist_id(valor_id):
            
            insert=("Insert into PAGO VALUES( {} ,'{}' ,{} ,{},{}) ".format(valor_id,fecha,idmet,monto,cliente_id))
            print(insert)

            
            cursor.execute(insert)
            conecion.commit()
        
        else:
            self.mensajes.setText("EL ID YA EXISTE")
            self.mensajes.execute

        
    def exist_id(self,num_id):
        #consulta BD srvicio
        
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        verific=('select id_met FROM PAGO WHERE ID_PAGO={} '.format(num_id))
        cursor=conecion.cursor()
        resultado=cursor.execute(verific).fetchall()

        return len(resultado) >0
 