   #--------------------------Comandos ORACLE--------------------------#
         #Conecta con BD
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()

        consulta= ('SELECT ID_Pago ,RAZ_SOC,METODO,FECHA FROM PAGO  JOIN CLIENTE USING (ID_CLI) JOIN METODO_PAGO USING (ID_MET) ')
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
        