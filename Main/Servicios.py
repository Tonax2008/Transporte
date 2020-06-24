from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget ,QTableWidgetItem,QErrorMessage, QMessageBox
import cx_Oracle
class Servicios(object):

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
        Form.setWindowTitle("SERVICIOS")


        self.mensajes= QMessageBox()


        #------------------------------------TABLA CONTENODR BD------------------------------------------# 
        
        #define la tabla
        self.tableWidget = QtWidgets.QTableWidget(Form)
        #Size de la tabla cordenadas (L,R,U,D)
        self.tableWidget.setGeometry(QtCore.QRect(23, 130, 1001, 651))
        #Nombre de la tablas
        self.tableWidget.setObjectName("tableWidget")
        #Columnas de la tabla
        self.tableWidget.setColumnCount(8)
        #fila de la tabla
        self.tableWidget.setRowCount(26)

       
        # Titulo a cada columna
        self.tableWidget.setItem(0,0,QTableWidgetItem("ID "))
        self.tableWidget.setItem(0,1,QTableWidgetItem("FECHA"))
        self.tableWidget.setItem(0,2,QTableWidgetItem("DESCRIPCION"))
        self.tableWidget.setItem(0,3,QTableWidgetItem("ID VIAJE"))
        self.tableWidget.setItem(0,4,QTableWidgetItem("ID PAGO"))
        self.tableWidget.setItem(0,5,QTableWidgetItem("ID UNIDAD"))
        self.tableWidget.setItem(0,6,QTableWidgetItem("ID EMPLEADO"))
        self.tableWidget.setItem(0,7,QTableWidgetItem("ID CLIENTE"))

        #Conecta BD
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()


        #AGREGAR COMOBOX PARA EVITAR BUSACR VARIOS ID

        consulta= ('SELECT ID_SER,FECHA,DESCRIPCION,ID_VIA,ID_PAGO,ID_UNI,ID_EMP,ID_CLI FROM SERVICIO')
        datos=cursor.execute(consulta).fetchall()
        conecion.close()

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


        self.CAMPO_7 = QtWidgets.QLabel(Form)
        self.CAMPO_7.setGeometry(QtCore.QRect(710, 60, 71, 16))
        self.CAMPO_7.setObjectName("CAMPO_7")


        self.CAMPO_8 = QtWidgets.QLabel(Form)
        self.CAMPO_8.setGeometry(QtCore.QRect(810, 60, 71, 16))
        self.CAMPO_8.setObjectName("CAMPO_8")

        
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


        self.lineEdit_C7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_C7.setGeometry(QtCore.QRect(710, 80, 81, 21))
        self.lineEdit_C7.setObjectName("lineEdit_C7")


        self.lineEdit_C8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_C8.setGeometry(QtCore.QRect(810, 80, 81, 21))
        self.lineEdit_C8.setObjectName("lineEdit_8")



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
        self.CAMPO_2.setText( "FECHA")
        self.CAMPO_3.setText( "DESCRIPCION")
        self.CAMPO4.setText( "ID VIAJE")
        self.CAMPO_5.setText( "ID_PAGO")
        self.CAMPO_6.setText( "ID_UNIDAD")
        self.CAMPO_7.setText( "EMPLEADO")
        self.CAMPO_8.setText( "CLIENTE")
        self.comboBox.setItemText(0,  "FIL1")
        self.comboBox.setItemText(1,  "FIL2")
        self.comboBox.setItemText(2,  "FIL3")

   
   
    def insertar(self):


        li_id=self.lineEdit_C1.text().strip()
        li_FECHA=self.lineEdit_C2.text().strip()
        li_DESCR=self.lineEdit_C3.text().strip()
        li_IDVIA=self.lineEdit_C4.text().strip()
        li_IDPAGO=self.lineEdit_C5.text().strip()
        li_IDUNI=self.lineEdit_C6.text().strip()
        li_IDEMP=self.lineEdit_C7.text().strip()
        li_IDCLI=self.lineEdit_C8.text().strip()

        
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()

        if not self.exist_id(li_id):
            
            insert=("Insert into SERVICIO VALUES( {} ,'{}' ,'{}' ,{},{},{},{},{},{}) ".format(li_id,li_FECHA,li_DESCR,li_IDVIA,li_IDPAGO,li_IDUNI,li_IDEMP,li_IDCLI))
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
            id_ser=self.tableWidget.item(i,0).text()
            id_1=self.tableWidget.item(i,1).text()
            id_2=self.tableWidget.item(i,2).text()           
            id_3=self.tableWidget.item(i,3).text()
            id_4=self.tableWidget.item(i,4).text()
            id_5=self.tableWidget.item(i,5).text()
            id_5=self.tableWidget.item(i,6).text()
            id_6=self.tableWidget.item(i,7).text()
            id_7=self.tableWidget.item(i,8).text()
            
            
           
            #self.tableWidget.removeRow(i)
            update=("UPDATE  SERICIO SET FECHA={},DESCRIPCION='{}',ID_VIA={},ID_PAGO={},ID_UNI={},ID_EMP={},ID_CLI={} WHERE ID_SER={}".format(id_1,id_2,id_3,id_4,id_5,id_6,id_7, id_ser))
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
            delate="DELETE FROM SERVICIO WHERE ID_SER={}".format(id_delate)
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
 