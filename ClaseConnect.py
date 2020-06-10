import pymysql

class ClaseConnect():
    def __init__ (self):
        self.CrearConnect()
        self.AbrirConexion()
    
    def CrearConnect(self):
        self.db = pymysql.connect(
            host="localhost", 
            port=3306, 
            user="root",
            passwd="", 
            db="futbol"
        )

    def AbrirConexion(self):
        self.cursor = self.db.cursor() 
    
    def EjecutarSQL(self, sql):
        self.cursor.execute(sql)
    
    def DevolverDatos(self):
        return self.cursor.fetchall()

    def DevolverActualización(self):
        return self.cursor.fechone()

    def CerrarBaseDatos(self):
        self.db.close()

    def RealizarCambio(self):
        self.db.commit()
    
    def NoRealizarCambio(self):
        self.db.rollback()