import sqlite3
import mysql.connector


class Classe_Banco(object):
    def __init__(self):
        super().__init__()


    def conectar(self):
            bc = sqlite3.connect('banco.db')
            cur = bc.cursor() 
            cur.execute("SELECT *FROM informacoes")
            dados_lidos = cur.fetchall()
            ip = dados_lidos[0][0]
            porta = dados_lidos[0][1]
            usuario = dados_lidos[0][2]
            senha = dados_lidos[0][3]
            self.query = mysql.connector.connect(
                host=ip,
                user=usuario,
                port=porta,
                password=senha)
            self.cursorr = self.query.cursor() 