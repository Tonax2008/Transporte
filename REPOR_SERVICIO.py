 # Titulo a cada columna
        self.tableWidget.setItem(0,0,QTableWidgetItem("Cliente"))
        self.tableWidget.setItem(0,1,QTableWidgetItem("Descripcion"))
        self.tableWidget.setItem(0,2,QTableWidgetItem("Id_Viaje"))
        self.tableWidget.setItem(0,3,QTableWidgetItem("Monto"))
        self.tableWidget.setItem(0,4,QTableWidgetItem("Unidad"))
        self.tableWidget.setItem(0,5,QTableWidgetItem("Empleado"))

        #Conecta BD
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()


        #AGREGAR COMOBOX PARA EVITAR BUSACR VARIOS ID

        consulta= ('select  RAZ_SOC,DESCRIPCION , ID_VIA,MONTO,ID_UNI,NOMBRE FROM SERVICIO JOIN CLIENTE USING (ID_CLI) JOIN PAGO USING (ID_PAGO) JOIN EMPLEADO USING (ID_EMP) JOIN UNIDAD USING   (ID_UNI) ')
        datos=cursor.execute(consulta).fetchall()

        if len (datos) >0:
            fila =1
            for p in datos:
                columna=1
                for c in p:
                    celda=QTableWidgetItem(str(c))
                    self.tableWidget.setItem(fila,columna,celda)
                    columna +=1
                fila +=1
