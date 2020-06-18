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

     #-------------------------------------------------- FUNCION Interfaz CONSULTA -----------------------------------------------------------#

    def setupUi(self, Form):


        #------------------------------------VENTANA PRINCIPAL------------------------------------------#
        #define una venata
        Form.setObjectName("Form")
        #Dedine tamaño de la ventana principal
        Form.resize(1049, 833)
        #Nombre de la ventana 
        Form.setWindowTitle("OFICINAS")

        self.mensajes= QMessageBox()


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
        self.tableWidget.setRowCount(20)

        # Titulo a cada columna
        self.tableWidget.setItem(0,0,QTableWidgetItem("ID OFICINA"))
        self.tableWidget.setItem(0,1,QTableWidgetItem("EMPRESA"))
        self.tableWidget.setItem(0,2,QTableWidgetItem("TELEFONO"))
        self.tableWidget.setItem(0,3,QTableWidgetItem("CORREO"))
        self.tableWidget.setItem(0,4,QTableWidgetItem("DIRECCION"))
        
       #Conecta DB
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()


        consulta= ('SELECT ID_OFI,RAZ_SOC,TELEFONO,CORREO FROM OFICINA JOIN CORREO USING (ID_COR) ')
        datos=cursor.execute(consulta).fetchall()
        

        #Consutlta direccion 
        adress=('SELECT CALLE , COLONIA,CP,DELEGACION,NO_INT,NO_EXT,ESTADO FROM OFICINA JOIN DIRECCION USING(ID_DIR) JOIN ESTADO USING (ID_EST) ')
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
                self.tableWidget.setItem(fila,4,celda)
                    
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

        #---Boton Buscar---#

        self.BT_BUSCAR = QtWidgets.QPushButton(Form)
        self.BT_BUSCAR.setGeometry(QtCore.QRect(710, 10, 113, 32))
        self.BT_BUSCAR.setObjectName("BT_BUSCAR")

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

        #---cuadro de buscar--#
        # Declara un text edit 
        self.lineEdit_BUSCAR = QtWidgets.QLineEdit(Form)
        #Size text edit
        self.lineEdit_BUSCAR.setGeometry(QtCore.QRect(400, 20, 291, 21))
        self.lineEdit_BUSCAR.setObjectName("lineEdit_BUSCAR")

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
        self.BT_BUSCAR.setText( "BUSCAR")
        self.BT_REGRESAR.setText( "REGRESAR")
        self.CAMPO_1.setText( "ID")
        self.CAMPO_2.setText( "NOMBRE")
        self.CAMPO_3.setText( "TELEFONO")
        self.CAMPO4.setText( "DIRECCION")
        self.CAMPO_5.setText( "CORREO")
        
        self.comboBox.setItemText(0,  "FIL1")
        self.comboBox.setItemText(1,  "FIL2")
        self.comboBox.setItemText(2,  "FIL3")

    def insertar(self):


        #DECLARA VARIABLES DE LOS EDITLABEL PARA PODER INSERTAR
        li_id=self.lineEdit_C1.text().strip()
        li_NOMBRE=self.lineEdit_C2.text().strip()
        li_TELEFONO=self.lineEdit_C3.text().strip()
        li_DIRE=self.lineEdit_C4.text().strip()
        li_EMAIL=self.lineEdit_C5.text().strip()
      

        
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()

       


        #VERIFICA QUE NO EXISTA UN ID PK REPETIDO ANTES DE INSERTAR
        if not self.exist_id(li_id):
            
            insert=("Insert into OFICINA VALUES( {} ,{} ,{} ,{},'{}') ".format(li_id,li_TELEFONO,li_EMAIL,li_DIRE,li_NOMBRE))
            print(insert)

            cursor.execute(insert)
            conecion.commit()
        
        else:
            self.mensajes.setText("EL ID YA EXISTE")
            self.mensajes.execute


        #FUNCION COMPUREBA DUPLICIDAD DE PK ID
    def exist_id(self,num_id):
        #consulta BD srvicio
        
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        verific=('select id_met FROM PAGO WHERE ID_PAGO={} '.format(num_id))
        cursor=conecion.cursor()
        resultado=cursor.execute(verific).fetchall()

        return len(resultado) >0

