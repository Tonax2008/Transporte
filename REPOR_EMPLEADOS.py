# Titulo a cada columna
        self.tableWidget.setItem(0,0,QTableWidgetItem("NOMBRE"))
        self.tableWidget.setItem(0,1,QTableWidgetItem("APELLIDO"))
        self.tableWidget.setItem(0,2,QTableWidgetItem("APELLIDO"))
        self.tableWidget.setItem(0,3,QTableWidgetItem("TELEFONO"))
        self.tableWidget.setItem(0,4,QTableWidgetItem("CORREO"))
        self.tableWidget.setItem(0,5,QTableWidgetItem("# SEGURO"))
        self.tableWidget.setItem(0,6,QTableWidgetItem("DIRECCION"))




       #Conecta con la BD
        conecion = cx_Oracle.connect("TRANS/terreno4@localhost:1521/XEPDB1")
        cursor=conecion.cursor()


        #Consutla 
        consulta= ('SELECT NOMBRE, APE_PAT ,APE_MAT ,TELEFONO,CORREO,NO_SEG FROM EMPLEADO JOIN CORREO USING (ID_COR) ')
        datos=cursor.execute(consulta).fetchall()
        
        #Consutlta direccion 
        adress=('SELECT CALLE , COLONIA,CP,DELEGACION,NO_INT,NO_EXT,ESTADO FROM EMPLEaDO JOIN DIRECCION USING(ID_DIR) JOIN ESTADO USING (ID_EST) ')
        direccion= cursor.execute(adress).fetchall()
        
        
        
        
        #ciclo para recorrer tabla BD
        if len (datos) >0:
            fila =1
            for p in datos:
                columna=0
                for c in p:
                    celda=QTableWidgetItem(str(c))

                    #Imprime dentro de la tabla
                    self.tableWidget.setItem(fila,columna,celda)
                    #print(str(c))
                    columna +=1
                fila +=1

        
        #Ciclo para rrecorer he imprimir dicrecciones BD

        if len (direccion) >0:
            fila=1

            for g in direccion:
                

                
                celda=QTableWidgetItem(str(g))
                #INICIA FILA 6
                self.tableWidget.setItem(fila,6,celda)
                    
                fila +=1
