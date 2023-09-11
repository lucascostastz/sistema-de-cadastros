from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6 import QtWidgets
import sys
import sqlite3
import mysql.connector
from time import sleep
from Janela_Inicio import Classe_Inicio
from Form_Login import Ui_Form_Login
from Janela_Cria_Banco import Classe_Tela_Cria_Banco


class Classe_Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login = Ui_Form_Login()
        self.login.setupUi(self)
        self.janela_Inicio = Classe_Inicio()
        self.Janela_cria_Banco = Classe_Tela_Cria_Banco()
        self.login.Lb_Background.setPixmap(
        QPixmap("..\img\Banner_LC.png"))
        self.conecta_banco()

        self.login.Bt_Login.clicked.connect(self.verifica_login)
        self.login.Bt_Sair.clicked.connect(self.sair_login)
        self.login.Bt_check.clicked.connect(self.password_check)
        self.login.Bt_Conectar.clicked.connect(self.conectar)
        self.login.Bt_Desconectar.clicked.connect(self.desconectar)
        self.login.Tx_Senha.returnPressed.connect(self.verifica_login)
        self.login.Tx_Usuario.returnPressed.connect(self.muda_tx_senha)


    def muda_tx_senha(self):
        self.login.Tx_Senha.setFocus()


        self.login.Bt_Tela_Login.clicked.connect(
        lambda: self.login.stackedWidget.setCurrentWidget(self.tela_login()))
        self.tela_login()
    
    def tela_login(self):
        self.login.Bt_Tela_Login.clicked.connect(
        lambda: self.login.stackedWidget.setCurrentWidget(self.login.Login))


        self.login.Bt_config_banco.clicked.connect(
        lambda: self.login.stackedWidget.setCurrentWidget(self.tela_banco()))
        self.tela_banco()

    def tela_banco(self):
        self.login.Bt_config_banco.clicked.connect(
        lambda: self.login.stackedWidget.setCurrentWidget(self.login.Banco))
        

    def sair_login(self):
        self.close()


    def chama_Janela_Inicio(self):
       self.janela_Inicio.show()


    def conecta_banco(self):
        self.bc = sqlite3.connect('banco.db')
        self.cur = self.bc.cursor() 
        self.cur.execute("SELECT *FROM informacoes")
        dados_lidos = self.cur.fetchall()
        ip = dados_lidos[0][0]
        porta = dados_lidos[0][1]
        usuario = dados_lidos[0][2]
        senha = dados_lidos[0][3]
        self.banco = mysql.connector.connect(
            host=ip,
            user=usuario,
            port=porta,
            password=senha)
        self.cursorr = self.banco.cursor()
        self.cursorr.execute("use pdv")
        
        

    def verifica_login(self):
        try:
            login = self.login.Tx_Usuario.text()
            senha2 = self.login.Tx_Senha.text()
            self.conecta_banco()
            self.cursorr.execute(
            "SELECT senha1, nivel_de_acesso FROM pdv.usuarios WHERE login ='{}'".format(login))
            senha_db = self.cursorr.fetchall()        
            try:
                if senha2 == senha_db[0][0] and (senha_db[0][1]) == 'ADMINISTRADOR':
                    self.carregar()
                    self.close()           
                    self.janela_Inicio.showMaximized()  
                    self.bc.close()
                elif senha2 == senha_db[0][0] and (senha_db[0][1]) == 'USUÁRIO':
                    self.carregar()
                    self.close()        
                    self.janela_Inicio.showMaximized()
                    self.bc.close()
                else:
                    self.login.Lb_Info.setText("Dados de login incorretos!")    
                    self.bc.close()
            except:
                self.login.Lb_Info.setText("Dados de login incorretos!")           
                self.bc.close()
        except:
            self.login.Lb_Info_banco.setText("Erro ao conectar ao banco de dados!")
            self.bc.close()
        

    def carregar(self):
        self.login.Tx_Usuario.clear()
        self.login.Tx_Senha.clear()
        self.login.Lb_Info.setText("")
        carregando = self.login.Lb_Info2.setText("Carregando...")
        print(carregando)
        self.login.my_progressBar.show()
        sleep(0.5)
        self.login.my_progressBar.setValue(10)
        sleep(0.5)
        self.login.my_progressBar.setValue(20)
        sleep(0.5)
        self.login.my_progressBar.setValue(30)
        sleep(0.5)
        aguarde = self.login.Lb_Info2.setText("Aguarde...")
        print(aguarde)
        self.login.my_progressBar.setValue(40)
        sleep(0.5)
        self.login.my_progressBar.setValue(50)
        sleep(0.5)
        self.login.my_progressBar.setValue(60)
        sleep(0.5)
        iniciando = self.login.Lb_Info2.setText("Iniciando o sistema...")
        print(iniciando)
        self.login.my_progressBar.setValue(70)
        sleep(0.5)
        self.login.my_progressBar.setValue(80)
        sleep(0.3)
        self.login.my_progressBar.setValue(90)
        sleep(0.1)
        self.login.my_progressBar.setValue(100)
        sleep(0.5)
        self.login.my_progressBar.close()


    def password_check(self):      
        bt = self.janela_Inicio.sender()
        if bt.isChecked() == True:
            self.login.Tx_Senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:    
            self.login.Tx_Senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  


    def conectar(self):
        try:
            host = self.login.Tx_Host.text()
            port = self.login.Tx_Porta.text()
            user = self.login.Tx_User.text()
            password = self.login.Tx_Password.text()
            bic = sqlite3.connect('banco.db')
            cursorr = bic.cursor() 
            cursorr.execute("DELETE FROM informacoes")
            bic.commit()
            if host == "":
                self.alt_cad_em_branco()
            elif port == "":
                    self.alt_cad_em_branco()
            elif user == "":
                    self.alt_cad_em_branco()
            else:
                cursorr.execute("INSERT INTO informacoes (ip,porta,usuario,senha) VALUES('" +
                    host+"','"+port+"','"+user+"','"+password+"')")
                bic.commit()
                bic.close()
                self.login.LB_Conectado.setText('Conectado...')
                self.login.LB_Desconectado.setText('')
                
        except:
            print("Erro ao conectar ao banco de dados!")  
        

    def desconectar(self):
            bic = sqlite3.connect('banco.db')
            cursorr = bic.cursor() 
            cursorr.execute("DELETE FROM informacoes")
            bic.commit()
            bic.close()
            self.login.LB_Desconectado.setText('Desconectado...')
            self.login.LB_Conectado.setText('')


    def limpar_campos(self):
        self.login.Tx_Host.clear()
        self.login.Tx_Porta.clear()
        self.login.Tx_Usuario.clear()
        self.login.Tx_Senha.clear()


    def alt_cad_em_branco(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Complete os Campos em Branco!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()


    def sair_config_banco(self):
        self.login.Tx_Host.clear()
        self.login.Tx_Porta.clear()
        self.login.Tx_Usuario.clear()
        self.login.Tx_Senha.clear()


if __name__ == '__main__':
    try:
        app =  QApplication(sys.argv)
        sleep(3)
        window = Classe_Login()
        window.show()
        (app.exec())
    except:
        window2 = Classe_Tela_Cria_Banco()
        window2.show()
        (app.exec())