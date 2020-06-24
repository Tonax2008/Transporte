from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget ,QTableWidgetItem,QErrorMessage, QMessageBox
import cx_Oracle
class Clientes(object):

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

    #-------------------------------------------------- FUNCION Interfaz CONSULTA -----------------------------------------------------------#

    def setupUi(self, Form):


        #------------------------------------VENTANA PRINCIPAL------------------------------------------#
        #define una venata
        Form.setObjectName("Form")
        #Dedine tamaño de la ventana principal
        Form.resize(1049, 833)
        #Nombre de la ventana 
        Form.setWindowTitle("CLIENTES")


        self.mensajes= QMessageBox()


        #------------------------------------TABLA CONTENODR BD------------------------------------------# 
        
        #define la tabla
        self.tableWidget = QtWidgets.QTableWidget(Form)
        #Size de la tabla cordenadas (L,R,U,D)
        self.tableWidget.setGeometry(QtCore.QRect(23, 130, 1001, 651))
        #Nombre de la tablas
        self.tableWidget.setObjectName("tableWidget")
        #Columnas de la tabla
        self.tableWidget.setColumnCount(4)
        #fila de la tabla
        self.tableWidget.setRowCount(20)

        #Titulo de columna
        self.tableWidget.setItem(0,0,QTableWidgetItem("CLIENTE"))
        self.tableWidget.setItem(0,1,QTableWidgetItem("RFC"))
        self.tableWidget.setItem(0,2,QTableWidgetItem("PAGINA WEB"))
        self.tableWidget.setItem(0,3,QTableWidgetItem("Direccion"))
        
       #Conecta BD
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()


        consulta= ('select RAZ_SOC , RFC,CORREO ,PAG_WEB FROM CLIENTE JOIN CORREO USING (ID_COR)')
        datos=cursor.execute(consulta).fetchall()

        #Consutlta direccion 
        adress=('SELECT CALLE , COLONIA,CP,DELEGACION,NO_INT,NO_EXT,ESTADO FROM CLIENTE JOIN DIRECCION USING(ID_DIR) JOIN ESTADO USING (ID_EST) ')
        direccion= cursor.execute(adress).fetchall()
        
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
        
        #Ciclo para rrecorer he imprimir dicrecciones BD

        if len (direccion) >0:
            fila=1

            for g in direccion:
                

                
                celda=QTableWidgetItem(str(g))
                self.tableWidget.setItem(fila,3,celda)
                    
                fila +=1
        
       

        #------------INSTERT-------------#



        #------------------------------------ BOTONES -----------------------------------------#

        #---Boton insertar---#
        
        #Declara un boton
        self.BT_INSERTAR = QtWidgets.QPushButton(Form)
        #Size boton
        self.BT_INSERTAR.setGeometry(QtCore.QRect(242, 12, 113, 32))
        #Nombre del objeto 
        self.BT_INSERTAR.setObjectName("BT_INSERTAR")
        self.BT_INSERTAR.clicked.connect(self.insertar)


        #---Boton Editar---#

        self.BT_EDITAR = QtWidgets.QPushButton(Form)
        self.BT_EDITAR.setGeometry(QtCore.QRect(127, 12, 113, 32))
        self.BT_EDITAR.setObjectName("BT_EDITAR")
        self.BT_EDITAR.clicked.connect(self.update)

        #---Boton ELIMINAR---#

        self.BT_ELIMINAR = QtWidgets.QPushButton(Form)
        self.BT_ELIMINAR.setGeometry(QtCore.QRect(710, 10, 113, 32))
        self.BT_ELIMINAR.setObjectName("BT_ELIMINAR")
        #CONECTA EL BOTON CON LA FUNCION ELIMINAR
        self.BT_ELIMINAR.clicked.connect(self.Eliminar)

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


        self.CAMPO_6 = QtWidgets.QLabel(Form)
        self.CAMPO_6.setGeometry(QtCore.QRect(610, 60, 71, 16))
        self.CAMPO_6.setObjectName("CAMPO_6")
        
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


        self.lineEdit_C6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_C6.setGeometry(QtCore.QRect(610, 80, 81, 21))
        self.lineEdit_C6.setObjectName("lineEdit_C6")

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
        self.CAMPO_1.setText( "ID")
        self.CAMPO_2.setText( "EMPRESA")
        self.CAMPO_3.setText( "RFC")
        self.CAMPO4.setText( "PAG WEB")
        self.CAMPO_5.setText( "CORREO")
        self.CAMPO_6.setText( "DIRECCION")
        
        self.comboBox.setItemText(0,  "FIL1")
        self.comboBox.setItemText(1,  "FIL2")
        self.comboBox.setItemText(2,  "FIL3")



    def insertar(self):


        li_idcli=self.lineEdit_C1.text().strip()
        li_RazonSoc=self.lineEdit_C2.text().strip()
        li_RFC=self.lineEdit_C3.text().strip()
        li_pagweb=self.lineEdit_C4.text().strip()
        li_idcor=self.lineEdit_C5.text().strip().lower()
        li_iddir=self.lineEdit_C6.text().strip().lower()


        
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()

        #Busca el id en la tabla correo  que corresponda al correo ingresado
        busqueda_1=("Select id_cor from CORREO  where METODO= '{}'".format(li_idcor))
        resultado_1=cursor.execute(busqueda_1).fetchall()

        #Busca el id en la tabla clientes con el cliente que corresponda
        busqueda_2=("Select id_cli from cliente  where RAZ_SOC= '{}'".format(li_iddir))
        resultado_2=cursor.execute(busqueda_2).fetchall()

        #Convierte la tupla lista tomada de la BD a una lista
        #print(resultado_1)
        id_1=[x[0] for x in resultado_1]
        #print(metod)
        #Selecciona el primer valor de la lista para pasarlo a la consulta en insert
        t_id1=(id_1[0])
        #print(m_metod)

        id_2=[x[0]for x in resultado_2]
        t_id2=(id_2[0])


       

        if not self.exist_id(li_idcli):
            
            insert=("Insert into CLIENTE VALUES( {} ,'{}' ,'{}' ,'{}',{},{}) ".format(li_idcli,li_RazonSoc,li_RFC, li_pagweb,t_id1,t_id2))
            print(insert)

            
            cursor.execute(insert)
            conecion.commit()
        
        else:
            self.mensajes.setText("EL ID YA EXISTE")
            self.mensajes.execute
    
    def update (self):

        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()

        rows=self.tableWidget.selectionModel().selectedRows()
        index=[]
        
        for i in rows:
            index.append(i.row())
        index.sort(reverse=True)

        for i in index:
            id_CLI=self.tableWidget.item(i,0).text()
            id_1=self.tableWidget.item(i,1).text()
            print(id_1)
            id_2=self.tableWidget.item(i,2).text()
            print(id_2)
            id_3=self.tableWidget.item(i,3).text()
            print(id_3)
            id_4=self.tableWidget.item(i,4).text()
            print(id_4)
            id_5=self.tableWidget.item(i,5).text()
            print(id_5)
            id_5=self.tableWidget.item(i,6).text()
            print(id_5)
          
           
            #self.tableWidget.removeRow(i)
            update=("UPDATE  CLIENTE SET  RAZ_SOC='{}',RFC='{}',PAG_WEB='{}',ID_COR={},ID_DIR={}  WHERE ID_CLI={}".format(id_1,id_2,id_3,id_4,id_5, id_CLI))
            print(update)
            cursor.execute(update)
            conecion.commit()
        conecion.close()

    def Eliminar (self):

        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()

        rows=self.tableWidget.selectionModel().selectedRows()
        index=[]

        for i in rows:
            index.append(i.row())
        index.sort(reverse=True)
        for i in index:
            id_delate=self.tableWidget.item(i,0).text()
            self.tableWidget.removeRow(i)
            delate="DELETE FROM CLIENTE WHERE ID_CLI={}".format(id_delate)
            cursor.execute(delate)
            conecion.commit()
        conecion.close()

        
    def exist_id(self,num_id):
        #consulta BD srvicio
        
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        verific=('select id_met FROM PAGO WHERE ID_PAGO={} '.format(num_id))
        cursor=conecion.cursor()
        resultado=cursor.execute(verific).fetchall()

        return len(resultado) >0
 

