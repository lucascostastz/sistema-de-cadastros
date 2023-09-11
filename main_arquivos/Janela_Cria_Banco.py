from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from Form_Cria_Banco import Ui_Form_Cria_Banco
from PyQt6.QtWidgets import QMessageBox
from time import sleep
from cria_base_pdv import criar_tabelas


class Classe_Tela_Cria_Banco(QMainWindow):
    def __init__(self):
        super().__init__()
        self.janela_cria_banco = Ui_Form_Cria_Banco()
        self.janela_cria_banco.setupUi(self)
        self.janela_cria_banco.Bt_Sim.clicked.connect(self.carregar_progresbar)
        self.janela_cria_banco.Bt_Nao.clicked.connect(self.close)


    def carregar_progresbar(self):
        try:
            self.janela_cria_banco.label_banco.clear()
            self.janela_cria_banco.label_banco.setText("Criando o banco de dados") 
            self.janela_cria_banco.ProgressBar.show()
            sleep(1)
            self.janela_cria_banco.ProgressBar.setValue(10)
            sleep(0.5)
            self.janela_cria_banco.ProgressBar.setValue(20)
            sleep(0.5)
            self.janela_cria_banco.ProgressBar.setValue(30)
            sleep(0.5)
            self.janela_cria_banco.label_banco.setText("Criando Tabelas...")
            self.janela_cria_banco.ProgressBar.setValue(40)
            sleep(1)
            self.janela_cria_banco.ProgressBar.setValue(50)
            sleep(0.5)
            self.janela_cria_banco.ProgressBar.setValue(60)
            sleep(0.5)
            self.janela_cria_banco.ProgressBar.setValue(70)
            sleep(0.5)
            self.janela_cria_banco.ProgressBar.setValue(80)
            sleep(0.3)
            self.janela_cria_banco.label_banco.setText("Finalizando...")
            self.janela_cria_banco.ProgressBar.setValue(90)
            sleep(0.5)
            self.janela_cria_banco.ProgressBar.setValue(100)
            sleep(0.5)
            self.janela_cria_banco.ProgressBar.close()
            criar_tabelas()
            self.alt_sucesso()
            self.limpa_campos()
            self.close()           
        except:
            self.alt_erro()
            self.limpa_campos()


    def alt_sucesso(self):
        msg = QMessageBox()
        msg.setWindowTitle("Sucesso!")
        msg.setText("Banco de dados criado, abra o sistema novamente!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()
    
    def alt_erro(self):
        msg = QMessageBox()
        msg.setWindowTitle("Erro!")
        msg.setText("Erro, verifique o caminho do banco de dados!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()
        
    def limpa_campos(self):
        self.janela_cria_banco.label_banco.clear()
        self.janela_cria_banco.ProgressBar.setValue(0)
        
         
if __name__ == '__main__':
    app =  QApplication(sys.argv)
    sleep(3)
    window = Classe_Tela_Cria_Banco()
    window.show()
    (app.exec())
