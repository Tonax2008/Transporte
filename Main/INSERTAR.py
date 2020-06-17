from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget ,QTableWidgetItem,QErrorMessage, QMessageBox
import cx_Oracle
import Unidades

class InsertarDatosBD ( QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Unidades()
        self.ui.setupUi(self)
        self.ui.BT_INSERTAR.clicked.connect(self.conectar)

        self.show()

    def conectar(self):
        pass
    def insertar(self):
        nombre_tabla="Unidad"
        valor_id=""

        if not self.exist_id(nombre_tabla,valor_id):
            pass
        
        else:
            self.mensajes.setText("EL ID YA EXISTE")
            self.mensaje.execute

        
    def exist_id(self,tabla,num_id):
        #consulta BD srvicio
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()
        verific='select*FROM {} WHERE id={}'.format(tabla,num_id)
        resultado=cursor.execute(verific).fetchall()

        return len(resultado) >0

