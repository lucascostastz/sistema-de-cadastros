from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from form.Usuario.Form_Cad_Usuario import Ui_Form_Cad_Usuario


class Classe_Cad_Usuario(QMainWindow, Ui_Form_Cad_Usuario):
    def __init__(self):
        super(Classe_Cad_Usuario, self).__init__()
        self.setupUi(self)


        self.Bt_CancelarUsuario.clicked.connect(self.fechar_janela)

    def fechar_janela(self):
        self.limpa_campos()
        self.close()


    def limpa_campos(self):
        self.tx_nome.clear()
        self.tx_Login.clear()
        self.tx_Senha.clear()
        self.tx_Senha2.clear()
        self.cb_Nivel_Acesso.setCurrentIndex(0)
        self.cb_Permissoes.setCurrentIndex(0)
        
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Cad_Usuario()
    system.show()
    sys.exit(app.exec())