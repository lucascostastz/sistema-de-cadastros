from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from form.Cliente.Form_Cad_Clientes import Ui_Form_Cad_Clientes

class Classe_Cad_Cliente(QMainWindow, Ui_Form_Cad_Clientes):
    def __init__(self):
        super(Classe_Cad_Cliente, self).__init__()
        self.setupUi(self)
        self.Bt_Voltar.clicked.connect(self.fechar_janela)
        

    def fechar_janela(self):
        self.limpar_campos()
        self.close()
        

    def limpar_campos(self):
        self.tx_Nome.clear()
        self.tx_cpf.clear()
        self.tx_Endereco.clear()
        self.tx_Telefone.clear()
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Cad_Cliente()
    system.show()
    sys.exit(app.exec())