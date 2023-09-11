from PyQt6.QtWidgets import *
from PyQt6 import QtWidgets
from time import sleep
from form.Login.Form_Login import Ui_Form_Login

class Classe_Login(QMainWindow, Ui_Form_Login):
    def __init__(self):
        super(Classe_Login, self).__init__()
        self.setupUi(self)

        self.Bt_Sair.clicked.connect(self._fechar_janela)
        self.Bt_check.clicked.connect(self.password_check)
    
    def _fechar_janela(self):
        self.close()

    def carregar(self):
        self.Tx_Usuario.clear()
        self.Tx_Senha.clear()
        self.Lb_Info.setText("")
        carregando = self.Lb_Info2.setText("Carregando...")
        print(carregando)
        self.my_progressBar.show()
        sleep(0.5)
        self.my_progressBar.setValue(10)
        sleep(0.5)
        self.my_progressBar.setValue(20)
        sleep(0.5)
        self.my_progressBar.setValue(30)
        sleep(0.5)
        aguarde = self.Lb_Info2.setText("Aguarde...")
        print(aguarde)
        self.my_progressBar.setValue(40)
        sleep(0.5)
        self.my_progressBar.setValue(50)
        sleep(0.5)
        self.my_progressBar.setValue(60)
        sleep(0.5)
        iniciando = self.Lb_Info2.setText("Iniciando o sistema...")
        print(iniciando)
        self.my_progressBar.setValue(70)
        sleep(0.5)
        self.my_progressBar.setValue(80)
        sleep(0.3)
        self.my_progressBar.setValue(90)
        sleep(0.1)
        self.my_progressBar.setValue(100)
        sleep(0.5)
        self.my_progressBar.close()

        
    def password_check(self):      
        bt = self.sender()
        if bt.isChecked() == True:
            self.Tx_Senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:    
            self.Tx_Senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password) 

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Login()
    system.show()
    sys.exit(app.exec())