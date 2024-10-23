import mysql.connector
from banco import Banco

class Usuarios(object):
    def __init__(self,id_usuario=0,nome="",telefone="",email="",usuario="",senha=""):
        self.info = {}
        self.id_usuario = id_usuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha
        
    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO usuario SET(nome,telefone,email,usuario,senha)VALUES(%s,%s,%s,%s,%s)",
                            (self.nome,self.telefone,self.email,self.usuario,self.senha))
            banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso"
        except Exception as e:
            return f"Ocorreu um erro na inserção de usuário: {e}"
        
    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT usuario SET nome,telefone,email,usuario,senha VALUES %s,%s,%s,%s,%s WHERE id_usuario=%s",
                            (self.nome,self.telefone,self.email,self.usuario,self.senha,self.id_usuario))
            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso"
        except Exception as e:
            return f"Ocorreu um erro na atualização de usuário: {e}"