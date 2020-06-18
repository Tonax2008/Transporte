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