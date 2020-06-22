from PyQt5 import QtCore, QtGui, QtWidgets
import Servicios,Viajes,CONSULTA,Clientes,Unidades,Empleados,METODOPAGO,DIRECCION,OFICINA,CORREO
import Repor_Pagos,REPOR_EMPLEADOS
#REPOR_OFICINA,REPOR_SERVICIO,REPOR_VIAJES

class Ui_Page2(object):

    #-------------------------------------------- Funcion MOVER entre Pantallas -----------------------------------------------------#

    def openwindow(self,llamar):

        self.window = QtWidgets.QMainWindow()
        self.ui = llamar
        self.ui.setupUi(self.window)
        self.window.show()
    #-------------------------------------------- Funcion MOVER entre Pantallas -----------------------------------------------------#

    def openServicios(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Servicios.Servicios()
        self.ui.setupUi(self.window)
        self.window.show()

    #------------------------------------------------ Interfaz pantalla Main ---------------------------------------------------------#


    def setupUi(self, Form):

        #Name Object
        Form.setObjectName("Form")
        #size Window object 
        Form.resize(775, 663)
        #Maixo permitido Window size
        Form.setMaximumSize(QtCore.QSize(1111, 904))

        #-----centralwidget----#
        #Declara objeto contenedor 
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")

        #-----Subwindow(MdiAera)----#
        #Declara area para subwindow
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        #Tamaño del contenedor subwindow
        self.mdiArea.setGeometry(QtCore.QRect(9, 9, 711, 601))
        self.mdiArea.setObjectName("mdiArea")

        #Invoca para ser mostrado en pantalla
        Form.setCentralWidget(self.centralwidget)

        #-----MenuBar----#
        #declara menubar izquierdo
        self.menubar = QtWidgets.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 22))
        #?¿
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")

        #-----Menu Principal----#
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")

        #-----Pestaña Usuarios----#
        #Declara pestaña usuarios dentro del menu principal
        self.menuUSUARIOS = QtWidgets.QMenu(self.menubar)
        #Object Name
        self.menuUSUARIOS.setObjectName("menuUSUARIOS")

        #-----Pestana Tablas----#
        self.menuTABLAS = QtWidgets.QMenu(self.menubar)
        self.menuTABLAS.setObjectName("menuTABLAS")

        #-----Pestana Tablas----#
        self.menuBASES_DE_DATOS = QtWidgets.QMenu(self.menubar)
        self.menuBASES_DE_DATOS.setObjectName("menuBASES_DE_DATOS")

        #-----Pestana Tablas----#
        self.menuAYUDA = QtWidgets.QMenu(self.menubar)
        self.menuAYUDA.setObjectName("menuAYUDA")

        #Incoca en la interfaZ ¿?
        Form.setMenuBar(self.menubar)

        #-----Tool Bar Izquierda---#
        #declara despatañas del menubar
        self.toolBar = QtWidgets.QToolBar(Form)
        self.toolBar.setObjectName("toolBar")
        #Incoca en la interfaZ ¿?
        Form.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)

        #-----Tool Bar Arriba (Vacio)---#
        self.toolBar_2 = QtWidgets.QToolBar(Form)
        self.toolBar_2.setObjectName("toolBar_2")

        #Incoca en la interfaZ ¿?
        Form.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)

        #--------------------------------------------------Ventanas , Acciones , Opciones y Triggers -----------------------------------------------#

        #-----Ventana Usuarios---#
        #Declara sub ventana
        self.actionUSUARIO = QtWidgets.QAction(Form)
        #Declara propiedad el icono
        icon = QtGui.QIcon()
        #Asocia imagen con icono delcarado
        icon.addPixmap(QtGui.QPixmap("Img/valor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #Pone icono en la pestana
        self.actionUSUARIO.setIcon(icon)
        #ObjectName
        self.actionUSUARIO.setObjectName("actionUSUARIO")

        #-----Opcion Salir---#
        self.actionSALIR = QtWidgets.QAction(Form)
        self.actionSALIR.setObjectName("actionSALIR")

        #-----Opcion Servicios---#
        self.actionServicios = QtWidgets.QAction(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Img/entrega-rapida.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionServicios.setIcon(icon1)
        self.actionServicios.setObjectName("actionServicios")
        #enlaza ventanas importadas
        self.actionServicios.triggered.connect(lambda: self.openServicios())

        #-----Opcion Viajes---#
        self.actionVIAJES = QtWidgets.QAction(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Img/libro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVIAJES.setIcon(icon2)
        self.actionVIAJES.setObjectName("actionVIAJES")
        self.actionVIAJES.triggered.connect(lambda: self.openwindow(Viajes.Viajes()))

        #-----Opcion Pagos---#
        self.actionPAGOS = QtWidgets.QAction(Form)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Img/pagos_icono.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPAGOS.setIcon(icon3)
        self.actionPAGOS.setObjectName("actionPAGOS")
        self.actionPAGOS.triggered.connect(lambda: self.openwindow(Repor_Pagos.Reporte_pagos()))

        #-----Opcion Clientes---#
        self.actionCLIENTES = QtWidgets.QAction(Form)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Img/CLIENTE.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCLIENTES.setIcon(icon4)
        self.actionCLIENTES.setObjectName("actionCLIENTES")
        self.actionCLIENTES.triggered.connect(lambda: self.openwindow(Clientes.Clientes()))

        #-----Opcion Empleados---#
        self.actionEMPLEADOS = QtWidgets.QAction(Form)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Img/empleado-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEMPLEADOS.setIcon(icon5)
        self.actionEMPLEADOS.setObjectName("actionEMPLEADOS")
        self.actionEMPLEADOS.triggered.connect(lambda: self.openwindow(REPOR_EMPLEADOS.Reporte_Empleados()))

        #-----Opcion Unidades---#
        self.actionUNIDADES = QtWidgets.QAction(Form)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Img/camion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUNIDADES.setIcon(icon6)
        self.actionUNIDADES.setObjectName("actionUNIDADES")
        self.actionUNIDADES.triggered.connect(lambda: self.openwindow(Unidades.Unidades()))

      

        #-----Opcion Respaldos---#
        self.actionRESPALDOS = QtWidgets.QAction(Form)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Img/base-de-datos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRESPALDOS.setIcon(icon7)
        self.actionRESPALDOS.setObjectName("actionRESPALDOS")

        #-----Opcion Tutorial---#
        self.actionTUTORIAL = QtWidgets.QAction(Form)
        self.actionTUTORIAL.setObjectName("actionTUTORIAL")

        #-----Opcion Inicio---#
        self.actionInicio = QtWidgets.QAction(Form)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Img/carrera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInicio.setIcon(icon8)
        self.actionInicio.setObjectName("actionInicio")

        #-----Opcion Agregar---#
        self.actionAGREGAR = QtWidgets.QAction(Form)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Img/mas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAGREGAR.setIcon(icon9)
        self.actionAGREGAR.setObjectName("actionAGREGAR")

        #-----Opcion Ediatr---#
        self.menuEDITAR = QtWidgets.QMenu(self.menuBASES_DE_DATOS)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Img/lapiz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuEDITAR.setIcon(icon10)
        self.menuEDITAR.setObjectName("actionEDITAR")

        #Declara la parte de pagos incluyendo subpagos (SubMenu)
        self.menuPagos = QtWidgets.QMenu(self.menuEDITAR)
        self.menuPagos.setObjectName("menuPagos")

        #-----Opcion Eliminar---#
        self.actionELIMINAR = QtWidgets.QAction(Form)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("Img/salida.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionELIMINAR.setIcon(icon11)
        self.actionELIMINAR.setObjectName("actionELIMINAR")

        #submenu de editar
        self.actionServicios_2 = QtWidgets.QAction(Form)
        self.actionServicios_2.setObjectName("actionServicios_2")

        #Submenu Metodo de pago
        self.actionMetodo_de_Pago = QtWidgets.QAction(Form)
        self.actionMetodo_de_Pago.setObjectName("actionMetodo_de_Pago")


        self.actionServicios_2 = QtWidgets.QAction(Form)
        self.actionServicios_2.setObjectName("actionServicios_2")
        self.actionServicios_2.triggered.connect(lambda: self.openwindow(Servicios.Servicios()))
        

        self.actionCliente = QtWidgets.QAction(Form)
        self.actionCliente.setObjectName("actionCliente")
        self.actionCliente.triggered.connect(lambda: self.openwindow(Clientes.Clientes()))
        

        self.actionEmpleados = QtWidgets.QAction(Form)
        self.actionEmpleados.setObjectName("actionEmpleados")
        self.actionEmpleados.triggered.connect(lambda: self.openwindow(Empleados.Empleados()))

        self.actionViajes = QtWidgets.QAction(Form)
        self.actionViajes.setObjectName("actionViajes")
        self.actionVIAJES.triggered.connect(lambda: self.openwindow(Viajes.Viajes()))

        self.actionDireccion = QtWidgets.QAction(Form)
        self.actionDireccion.setObjectName("actionDireccion")
        self.actionDireccion.triggered.connect(lambda: self.openwindow(DIRECCION.Direcciones()))

        self.actionOficina = QtWidgets.QAction(Form)
        self.actionOficina.setObjectName("actionOficina")
        self.actionOficina.triggered.connect(lambda: self.openwindow(OFICINA.Oficina()))

        self.actionUnidad = QtWidgets.QAction(Form)
        self.actionUnidad.setObjectName("actionUnidad")
        self.actionUnidad.triggered.connect(lambda: self.openwindow(Unidades.Unidades()))

        self.actionMetodo_de_Pago = QtWidgets.QAction(Form)
        self.actionMetodo_de_Pago.setObjectName("actionMetodo_de_Pago")
        self.actionMetodo_de_Pago.triggered.connect(lambda: self.openwindow(METODOPAGO.Metodo()))

        self.actionCorreos = QtWidgets.QAction(Form)
        self.actionCorreos.setObjectName("actionCorreos")
        self.actionCorreos.triggered.connect(lambda: self.openwindow(CORREO.Correo()))

        

        #-----Opcion ¿?---#
        self.action = QtWidgets.QAction(Form)
        self.action.setObjectName("action")

        #asocia ventanas con opciones
        self.menu.addAction(self.actionInicio)
        self.menuUSUARIOS.addAction(self.actionUSUARIO)
        self.menuUSUARIOS.addSeparator()
        self.menuUSUARIOS.addAction(self.actionSALIR)
        self.menuTABLAS.addAction(self.actionServicios)
        self.menuTABLAS.addAction(self.actionVIAJES)
        self.menuTABLAS.addAction(self.actionPAGOS)
        self.menuTABLAS.addAction(self.actionCLIENTES)
        self.menuTABLAS.addAction(self.actionEMPLEADOS)
        self.menuTABLAS.addAction(self.actionUNIDADES)
        self.menuTABLAS.addAction(self.actionOficina)
        self.menuBASES_DE_DATOS.addAction(self.menuEDITAR.menuAction())
        self.menuBASES_DE_DATOS.addSeparator()

        #Ventana de editar todas las tablas para consulta
        self.menuPagos.addAction(self.actionMetodo_de_Pago)
        self.menuEDITAR.addAction(self.actionServicios_2)
        self.menuEDITAR.addAction(self.actionCliente)
        self.menuEDITAR.addAction(self.menuPagos.menuAction())
        self.menuEDITAR.addAction(self.actionEmpleados)
        self.menuEDITAR.addAction(self.actionViajes)
        self.menuEDITAR.addAction(self.actionDireccion)
        self.menuEDITAR.addAction(self.actionOficina)
        self.menuEDITAR.addAction(self.actionUnidad)
        self.menuEDITAR.addAction(self.actionCorreos)

        self.menuBASES_DE_DATOS.addAction(self.actionAGREGAR)
        self.menuBASES_DE_DATOS.addAction(self.actionELIMINAR)
        self.menuBASES_DE_DATOS.addSeparator()
        self.menuBASES_DE_DATOS.addAction(self.actionRESPALDOS)
        self.menuAYUDA.addAction(self.actionTUTORIAL)
        self.menuAYUDA.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuUSUARIOS.menuAction())
        self.menubar.addAction(self.menuTABLAS.menuAction())
        self.menubar.addAction(self.menuBASES_DE_DATOS.menuAction())
        self.menubar.addAction(self.menuAYUDA.menuAction())
        self.toolBar.addAction(self.actionInicio)
        self.toolBar.addAction(self.actionCLIENTES)
        self.toolBar.addAction(self.actionEMPLEADOS)
        self.toolBar.addAction(self.actionAGREGAR)



        #mete textos  en los obejtos , muestra en la interfaz
        self.retranslateUi(Form)
        #Conecta los textos con botones
        QtCore.QMetaObject.connectSlotsByName(Form)


    #----------------------------------------------------Funcion Textos--------------------------------------------------------------------------#
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MainWindow"))
        self.menu.setTitle(_translate("Form", "."))
        self.menuUSUARIOS.setTitle(_translate("Form", "USUARIOS"))
        self.menuTABLAS.setTitle(_translate("Form", "CONSULTAS"))
        self.menuBASES_DE_DATOS.setTitle(_translate("Form", "BASES DE DATOS"))
        self.menuAYUDA.setTitle(_translate("Form", "AYUDA"))
        self.toolBar.setWindowTitle(_translate("Form", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("Form", "toolBar_2"))
        self.actionUSUARIO.setText(_translate("Form", "USUARIO"))
        self.actionSALIR.setText(_translate("Form", "SALIR"))
        self.actionServicios.setText(_translate("Form", "SERVICIOS"))
        self.actionVIAJES.setText(_translate("Form", "VIAJES"))
        self.actionPAGOS.setText(_translate("Form", "PAGOS"))
        self.actionCLIENTES.setText(_translate("Form", "CLIENTES"))
        self.actionEMPLEADOS.setText(_translate("Form", "EMPLEADOS"))
        self.actionUNIDADES.setText(_translate("Form", "UNIDADES"))
        
        self.actionRESPALDOS.setText(_translate("Form", "RESPALDOS"))
        self.actionTUTORIAL.setText(_translate("Form", "TUTORIAL"))
        self.actionInicio.setText(_translate("Form", "INICIO"))
        self.actionAGREGAR.setText(_translate("Form", "AGREGAR"))
        #self.menuEDITAR.setText(_translate("Form", "EDITAR "))
        self.actionELIMINAR.setText(_translate("Form", "ELIMINAR"))
        self.action.setText(_translate("Form", "?"))

        self.actionServicios_2.setText(_translate("Principal", "Servicios"))
        self.actionCliente.setText(_translate("Principal", "Cliente"))
        self.actionEmpleados.setText(_translate("Principal", "Empleados"))
        self.actionViajes.setText(_translate("Principal", "Viajes"))
        self.actionDireccion.setText(_translate("Principal", "Direccion"))
        self.actionOficina.setText(_translate("Principal", "Oficina"))
        self.actionUnidad.setText(_translate("Principal", "Unidad"))
        self.actionMetodo_de_Pago.setText(_translate("Principal", "Metodo de Pago"))
        self.actionCorreos.setText(_translate("Principal", "Correos"))

    #---------------------------------------------------- Funcion Boton Regresar--------------------------------------------------------------------------#    

    def button_handler_back(self):
        self.openwindow()
    