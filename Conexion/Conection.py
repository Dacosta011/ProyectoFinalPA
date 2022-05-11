from mysql import connector
from mysql.connector import Error


class Conection:
    def __init__(self):
        print("Conectando a la base de datos...")
    
    def conection(self):
        try:
            self.con = connector.connect(
                host = "localhost",
                user = "root",
                passwd = "",
                database = "universidad"
            )
            if self.con.is_connected():
                print("Conectado a la base de datos")
                return self.con
        except Error as e:
            print(e)
    
    def desconection(self):
        self.con.close()
        print("Desconectado de la base de datos")