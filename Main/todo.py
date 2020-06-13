from PyQt5 import QtCore, QtGui, QtWidgets
import venprin
import mysql.connector




class Ui_Form(object):

    def __init__(self):
        

        self.pantalla_2=venprin.Ui_Page2()

    def openwindow(self):

        
        self.window = QtWidgets.QMainWindow()
        self.ui = venprin.Ui_Page2()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(734, 428)
        self.label_username = QtWidgets.QLabel(Form)
        self.label_username.setGeometry(QtCore.QRect(160, 130, 121, 31))
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(Form)
        self.label_password.setGeometry(QtCore.QRect(160, 190, 111, 21))
        self.label_password.setObjectName("label_password")
        self.txt_input_username = QtWidgets.QLineEdit(Form)
        self.txt_input_username.setGeometry(QtCore.QRect(380, 140, 201, 21))
        self.txt_input_username.setObjectName("txt_input_username")
        self.txt_input_password = QtWidgets.QLineEdit(Form)
        self.txt_input_password.setGeometry(QtCore.QRect(380, 190, 201, 21))
        self.txt_input_password.setObjectName("txt_input_password")
        self.btn_submit = QtWidgets.QPushButton(Form)
        self.btn_submit.setGeometry(QtCore.QRect(380, 240, 211, 32))
        self.btn_submit.setObjectName("btn_submit")
        self.text_title = QtWidgets.QTextEdit(Form)
        self.text_title.setGeometry(QtCore.QRect(60, 10, 629, 51))
        self.text_title.setObjectName("text_title")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(390, 290, 191, 20))
        self.radioButton.setObjectName("radioButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login Page"))
        self.label_username.setText(_translate("Form", "Enter User Name"))
        self.label_password.setText(_translate("Form", "Enter Password"))
        self.btn_submit.setText(_translate("Form", "Ingresar"))




        self.btn_submit.clicked.connect(self.btn_submit_handler)


    def btn_submit_handler(self):
        val_pass = self.txt_input_password.text()
        val_username = self.txt_input_username.text()

        if val_pass == "admin" and val_username == "admin":
            print("welcome")
            print(self.radioButton.text())



            self.openwindow()

            #Page2.show()
            #self.ui.btn_sumbit.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(0))

#------------------------------------------------------------  VENTANA 2 -----------------------------------------------------------------------#


#------------------------------------------------------------  VENTANA 3-----------------------------------------------------------------------#



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())
