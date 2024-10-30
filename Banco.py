#Bernardo Behling Garcia
import mysql.connector

class Banco():
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="locahost",
            user="root",
            password="root",
            database="bernardo_db"
        )
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS usuario(id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                          nome text,
                          telefone text,
                          email text, 
                          usuario text, 
                          senha text)''')
        
        self.conexao.commit()
        c.close()