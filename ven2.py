from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Page3(object):

    def openwindow(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Page2()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, Form):
        


        #
        Form.setObjectName("Form")
        Form.resize(975, 709)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(13, 56, 681, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(242, 12, 113, 32))
        self.pushButton_3.setObjectName("Insertar")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(369, 16, 221, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(12, 12, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(127, 12, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(590, 10, 113, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        #

        self.pushButton_3.setText( "Insertar")
        self.pushButton.setText  ( "Filtrar")
        self.pushButton_2.setText ("Editar")
        self.pushButton_4.setText ("Buscar")

        self.btn_back = QtWidgets.QPushButton(Form)
        self.btn_back.setGeometry(QtCore.QRect(100, 100, 113, 32))
        self.btn_back.setObjectName("btn_back")
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def retranslateUi(self, Page2):
        _translate = QtCore.QCoreApplication.translate
        Page2.setWindowTitle(_translate("Page2", "Segunda"))


        #----------------------------------------------------Experimento--------------------------------------------------------------------------#
        

        #----------------------------------------------------FIN Experimento--------------------------------------------------------------------------#
       
        self.btn_back.clicked.connect(self.button_handler_back)

    def button_handler_back(self):
        self.openwindow()
