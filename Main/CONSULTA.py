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
        self.tableWidget.setItem(0,0,QTableWidgetItem("ID_PAGO"))                   #Titulo de cada celda de la tabla en la consulta
        self.tableWidget.setItem(0,1,QTableWidgetItem("FECHA"))                     #SetItem (fila,columna,texto)
        self.tableWidget.setItem(0,2,QTableWidgetItem("ID METODO"))
        self.tableWidget.setItem(0,3,QTableWidgetItem("MONTO"))
        self.tableWidget.setItem(0,4,QTableWidgetItem("ID CLIENTE"))


        #--------------------------Comandos ORACLE--------------------------#
         #Conecta con BD
        
        #try de coneccion a la BD
        try:
            
            conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")        #Define user , pass, puerto , conenedor he ip
            cursor=conecion.cursor()                                                    #Ejecuta la coneccion
        except Exception as err:                                                        #Exepcion si ocurre algun error al conectar ka BD

            self.mensajes.setWindowTitle("HOLA ME VES SOY UN TITULO")                   #Titulo de la ventana emergente
            self.mensajes.setText("Coneccion no lograda" )                              #Mensaje de la ventanaa emergente
            #self.mensajes.informativeText(err)                                         #Texto informativo de la ventana emergente con el error de oracle
            self.mensajes.setIcon(QMessageBox.Critical)                                 #Icono de la ventana emrgente 
            self.mensajes.exec_()                                                       #Ejecuta la ventana emergente
        
        else:           
            try:
                consulta= ('SELECT ID_PAGO ,FECHA ,ID_MET,MONTO,ID_CLI FROM PAGO')      #Defino la consulta a realizar en la bd
                datos=cursor.execute(consulta).fetchall()                               #EJECUTO CONSULTA Y REGRESO TODOS LO VALORES EN TUPLA
            

                #------------CONSULTAS-------------#
                #ciclo para recorrer tabla BD
                if len (datos) >0:
                    fila =1                                                             #RECORRE LA TUPLA HE IMPRIEME EN CADA CELDA CON
                    for p in datos:                                                     #SetItem(fila,columna,celda)
                        columna=0
                        for c in p:
                            celda=QTableWidgetItem(str(c))
                            self.tableWidget.setItem(fila,columna,celda)
                            columna +=1
                        fila +=1
            except Exception as err:                                                    #Exepcion a un error al ejecutar la consulta
                self.mensajes.setWindowTitle("HOLA ME VES SOY UN TITULO")               #Titulo vetana emergente
                self.mensajes.setText("Consulta Invalida")                              #Mensaje ventana Emergente
                self.mensajes.setIcon(QMessageBox.Warning)                              #Icono ventana emrgente
                self.mensajes.exec_()                                                   #Ejectua ventana emergente
            finally:
                conecion.close()                                                        #Cierra conecion con BD
       

        #------------------------------------ BOTONES -----------------------------------------#

        #---Boton insertar---#
        
        #Declara un boton y ereda el formato de ventana principal
        self.BT_INSERTAR = QtWidgets.QPushButton(Form)
        #Size boton
        self.BT_INSERTAR.setGeometry(QtCore.QRect(242, 12, 113, 32))
        #Nombre del objeto 
        self.BT_INSERTAR.setObjectName("BT_INSERTAR")
        #Conecta el botn con la funcion insertar 
        self.BT_INSERTAR.clicked.connect(self.insertar)


    #---Boton Editar---#

        #Declara un boton y ereda el formato de ventana principal
        self.BT_EDITAR = QtWidgets.QPushButton(Form)
        #Establece le tamaño del boton con cordenadas
        self.BT_EDITAR.setGeometry(QtCore.QRect(127, 12, 113, 32))
        self.BT_EDITAR.setObjectName("BT_EDITAR")
        #Conecta el botn con la funcion de update
        self.BT_EDITAR.clicked.connect(self.update)

        #---Boton ELIMINAR---#

        self.BT_ELIMINAR = QtWidgets.QPushButton(Form)
        self.BT_ELIMINAR.setGeometry(QtCore.QRect(710, 10, 113, 32))
        self.BT_ELIMINAR.setObjectName("BT_ELIMINAR")
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


        self.CAMPO_2 = QtWidgets.QLabel(Form)                               #Declara Objeto label para poner texto definido
        self.CAMPO_2.setGeometry(QtCore.QRect(240, 60, 71, 16))             #Tamaña del label
        self.CAMPO_2.setObjectName("CAMPO_2")                               #Etiqueta del objeto


        self.CAMPO_3 = QtWidgets.QLabel(Form)                                #Declara Objeto label para poner texto definido
        self.CAMPO_3.setGeometry(QtCore.QRect(330, 60, 71, 16))             #Tamaña del label
        self.CAMPO_3.setObjectName("CAMPO_3")                               #Etiqueta del objeto
        


        self.CAMPO4 = QtWidgets.QLabel(Form)                                #Declara Objeto label para poner texto definido
        self.CAMPO4.setGeometry(QtCore.QRect(420, 60, 71, 16))              #Tamaña del label
        self.CAMPO4.setObjectName("CAMPO4")                                 #Etiqueta del objeto


        self.CAMPO_5 = QtWidgets.QLabel(Form)                               #Declara Objeto label para poner texto definido
        self.CAMPO_5.setGeometry(QtCore.QRect(510, 60, 71, 16))             #Tamaña del label
        self.CAMPO_5.setObjectName("CAMPO_5")                               #Etiqueta del objeto


       

        
        #------------------------------------ Text Edit (barra de texto editable) -----------------------------------------#

        #---cuadro de Consulta--#
        # Declara un text edit 
        self.lineEdit_ELIMINAR = QtWidgets.QLineEdit(Form)
        #Size text edit
        self.lineEdit_ELIMINAR.setGeometry(QtCore.QRect(400, 20, 291, 21))
        self.lineEdit_ELIMINAR.setObjectName("lineEdit_ELIMINAR")

        #---cuadro de nombre--#
        self.lineEdit_C1 = QtWidgets.QLineEdit(Form)                                #Declara un obejto line edit para ingresar texto , parecido a un input
        self.lineEdit_C1.setGeometry(QtCore.QRect(130, 80, 81, 21))                 #Tamaño del line edit
        self.lineEdit_C1.setObjectName("lineEdit_C1")                               #Etiqueta del line edit


        self.lineEdit_C2 = QtWidgets.QLineEdit(Form)                                #Declara un obejto line edit para ingresar texto , parecido a un input
        self.lineEdit_C2.setGeometry(QtCore.QRect(230, 80, 81, 21))                 #Tamaño del line edit
        self.lineEdit_C2.setObjectName("lineEdit_C2")                               #Etiqueta del line edit

        #Declara combo Box
        self.lineEdit_C3 = QtWidgets.QComboBox(Form)
        self.lineEdit_C3.setGeometry(QtCore.QRect(320, 80, 81, 21))
        self.lineEdit_C3.setObjectName("lineEdit_C3")

        #Define el tamaño del listado dentro del combo box y crea los campos para ingresar la sopciones
        self.lineEdit_C3.addItem("")
        self.lineEdit_C3.addItem("")
        self.lineEdit_C3.addItem("")
        self.lineEdit_C3.addItem("")
        self.lineEdit_C3.addItem("")
        self.lineEdit_C3.addItem("")
        self.lineEdit_C3.addItem("")


        self.lineEdit_C4 = QtWidgets.QLineEdit(Form)                                #Declara un obejto line edit para ingresar texto , parecido a un input                                
        self.lineEdit_C4.setGeometry(QtCore.QRect(410, 80, 81, 21))                 #Tamaño del line edit
        self.lineEdit_C4.setObjectName("lineEdit_C4")                               #Etiqueta del line edit

        self.lineEdit_C5 = QtWidgets.QLineEdit(Form)                                #Declara un obejto line edit para ingresar texto , parecido a un input
        self.lineEdit_C5.setGeometry(QtCore.QRect(510, 80, 81, 21))                 #Tamaño del line edit
        self.lineEdit_C5.setObjectName("lineEdit_C5")                               #Etiqueta del line edit


        

        #---------------------- Caja de filtrar  con sus opciones-------------#

        self.comboBox = QtWidgets.QComboBox(Form)                                   #Declar un combo box en el cual se ingresa una lista a seleccionar
        self.comboBox.setGeometry(QtCore.QRect(30, 15, 71, 71))                     #Tamaño del combo boc
        self.comboBox.setObjectName("comboBox")
        #texto de las listas a seleccionar
        self.comboBox.addItem("")                                                   #Define el tamaño del listado dentro del combo box y crea los campos para ingresar la sopciones
        self.comboBox.addItem("")                                                   #Textto con cordenadas 0,1
        self.comboBox.addItem("")                                                   #texto con coredanas 0,2

        

        #textos de los botones y campos
        self.BT_INSERTAR.setText( "INSERTAR")                                       #Ingreso los textos de cada elemento declarado arriba
        self.BT_EDITAR.setText( "EDITAR")                                           #Se hizo de esta manera para mantener el orden al buscar    
        self.BT_ELIMINAR.setText( "ELIMINAR")                                       #Recomendado por python y pqt5 al general el codigo .py desde .ui
        self.BT_REGRESAR.setText( "REGRESAR")
        self.CAMPO_1.setText( "ID_PAGO")
        self.CAMPO_2.setText( "FECHA")
        self.CAMPO_3.setText( "METODO")
        self.CAMPO4.setText( "MONTO")
        self.CAMPO_5.setText( "CLIENTE")

        self.lineEdit_C3.setItemText(0,"Seleccionar")                               #Texto de los combo boxes con las cordenadas antes del texto
        self.lineEdit_C3.setItemText(1,"Efectivo")                                  #Cada cordena fue asoisada con el id que se le va pasar e las consultas de BD
        self.lineEdit_C3.setItemText(2,"Transferencia")
        self.lineEdit_C3.setItemText(3,"Deposito")
        self.lineEdit_C3.setItemText(4,"Cheque")
        self.lineEdit_C3.setItemText(5,"Criptomoneda")

        
        self.comboBox.setItemText(0,  "FIL1")                               #Texto de los combo boxes con las cordenadas antes del texto                                       
        self.comboBox.setItemText(1,  "FIL2")                               #Texto para el filtro 
        self.comboBox.setItemText(2,  "FIL3")                               #Falta definir consultas

    #Funcion para insertar nuevos datos dentro de la funcion de pagos 

    def insertar(self):


        #Pasa valores de los Text Edit 
        valor_id=self.lineEdit_C1.text().strip()
        fecha=self.lineEdit_C2.text().strip()
        monto=self.lineEdit_C4.text().strip()
        bus_clie=self.lineEdit_C5.text().strip()    
        #Toma el valor del ComboBox en int segun cordenadas de la posicion
        metodo= self.lineEdit_C3.currentIndex()

        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()


        #busqueda_1=("Select id_met from metodo_pago  where METODO= '{}'".format(bus_met))
        #resultado_1=cursor.execute(busqueda_1).fetchall()

        busqueda_2=("Select id_cli from cliente  where RAZ_SOC= '{}'".format(bus_clie))
        resultado_2=cursor.execute(busqueda_2).fetchall()

        #print(resultado_1)
        #metod=[x[0] for x in resultado_1]
        #print(metod)
        #t_metod=(metod[0])
        #print(m_metod)

        cliente=[x[0]for x in resultado_2]
        t_cliente=(cliente[0])

        
        #idmet=int(t_metod)
        #print(idmet)        
        cliente_id=t_cliente

        if not self.exist_id(valor_id):                                                                 #Verifica que no exista un ID repetido antes de ingresar
            
            insert=("Insert into PAGO VALUES( {} ,'{}' ,{} ,{},{}) ".format(valor_id,fecha,metodo,monto,cliente_id))    #consulta a la bd
            print(insert)
            cursor.execute(insert)                                                                                          #Ejecuta la consulta
            conecion.commit()                                                                                           #Realiza un commit en la BD
            conecion.close()                                                                            #Cierra coneccion la BD
        
        else:  
            #Mensaje emergenete cuando existe un ID repetido
            self.mensajes.setText("ID EXISTENE")                                                        #Mensahe de la ventana emergenrte                                                         
            self.mensajes.setIcon(QMessageBox.Critical)                                                 #Icono de la ventana emergente
            self.mensajes.informativeText("Ingrese otro ID")                                            #Texto informativo de la ventana emergente
            self.mensajes.exec_()                                                                       #Ejectua la ventana emergente

    #Funcion de elmimar registro de la BD

    def Eliminar (self):

        try:
            conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")                    #Crea una conexion 
            cursor=conecion.cursor()                                                                #Ejecuta la conexion
        except Exception as err:                                                                    #Exepcion  si no se puede conectar con la BD
            self.mensajes.setWindowTitle("HOLA ME VES SOY UN TITULO")                               #Mensaje de la ventana emergente
            self.mensajes.setText("Coneccion No Lograda")                                           
            self.mensajes.setIcon(QMessageBox.Critical)     
            self.mensajes.exec_()                                                                    #Ejecuta ventana emergente
        else:
            try:
                rows=self.tableWidget.selectionModel().selectedRows()                               #Toma el los valores d ela fila seleccionada en la tabla
                index=[]                                                                            #Crea un vector vacio
                
                if len(rows)>0:                                                                     #Verifica si tiene una cadena vacia en la fila
                
                    for i in rows:                                                                  #Recorre la fila
                        index.append(i.row())                           
                    index.sort(reverse=True)
                    for i in index:                                         
                        id_delate=self.tableWidget.item(i,0).text()                                     #Toma el primer valor de la fila con las cordenas (i,0)
                        self.tableWidget.removeRow(i)                                               #Elimina la fila seleccionada de la interfaz
                        delate=("DELETE FROM PAGO WHERE PAGO ID_PAGO={}".format(id_delate))         #crea una funcion BD para eliminar el registro de la BD
                        print(delate)   
                        cursor.execute(delate)                                                      #Ejecita el delate en la BD
                        conecion.commit()                                                           #Ejecuta un commit en la BD
                else:
                    self.mensajes.setText("SELECCIONE UNA FILA")                                    #error si no se selecciona la fila completa
                    self.mensajes.setIcon(QMessageBox.Warning)                                      #Icono de la ventana emrgente
                    self.mensajes.exec_()                                                           #Ejecuita vnetana emergente

            except Exception as err:                                                                #try si no se pudo eleminar la fila , problema en MYSQL

                
                self.mensajes.setText("ERROR AL ELIMINAR FILA SELECCIONADA")                        #Mensjae del erroe ventaba eergeb
                self.mensajes.setIcon(QMessageBox.Critical)                                         #icono de la ventana emrgene
                self.mensajes.setDetailedText("SELECCIONE TODA LA FILA"+ '\n' + "ACTUALICE LA TABLA")
                self.mensajes.exec_()                                                               #Ejecuta ventana emrgente
           

    def update (self):

        try:

            conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
            cursor=conecion.cursor()
        except Exception as err:

            self.mensajes.setText("ERROR DE CONECCION")
            self.mensajes.setIcon(QMessageBox.Warning)
            self.mensajes.exec_()

        else:

            try:
                rows=self.tableWidget.selectionModel().selectedRows()
                index=[]
                for i in rows:
                    index.append(i.row())
                index.sort(reverse=True)

                for i in index:
                    #TOma el valor de toda la fula y lo divide para poder volver a ingresar en el update
                    id_pago=self.tableWidget.item(i,0).text()
                    id_delate=self.tableWidget.item(i,1).text()
                    print(id_delate)
                    id_2=self.tableWidget.item(i,2).text()
                    print(id_2)
                    id_3=self.tableWidget.item(i,3).text()
                    print(id_3)
                    id_4=self.tableWidget.item(i,4).text()
                    print(id_4)

                    #self.tableWidget.removeRow(i)
                    update=("UPDATE  PAGO SET ID_MET={},MONTO={},ID_CLI={} WHERE ID_PAGO={}".format(id_2,id_3,id_4,id_pago))
                    print(update)
                    cursor.execute(update)
                    conecion.commit()
            except Exception as err:

                self.mensajes.setText("ERROR AL ALTERAR LA TABLA")
                self.mensajes.setIcon(QMessageBox.Critical)
                self.mensajes.setDetailedText("Ingrese un dato numerico en el campo id a modificar")
                self.mensajes.setStandardButtons(QMessageBox.Retry|QMessageBox.Cancel)
                self.mensajes.exec_()
            finally:
                conecion.close()


    #FUnicon id duplicado        
    def exist_id(self,num_id):
        #consulta BD srvicio
        
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        verific=('select id_met FROM PAGO WHERE ID_PAGO={} '.format(num_id))
        cursor=conecion.cursor()
        resultado=cursor.execute(verific).fetchall()

        return len(resultado) >0
    
    

