from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from form.Agendamento.Form_Agendamento import Ui_Form_Agendamento

class Classe_Agendamento(QMainWindow, Ui_Form_Agendamento):
    def __init__(self):
        super(Classe_Agendamento, self).__init__()
        self.setupUi(self)


        self.Bt_Can_Agendamento.clicked.connect(self.fechar_janela)
        self.lb_FotoLogo.setPixmap(
        QPixmap(".\img\Banner_LC.png"))
      

    def fechar_janela(self):
        self.limpar_campos()
        self.close()
        

    def limpar_campos(self):
        self.tx_Nome.clear()
        self.tx_Cpf.clear()
        self.tx_Endereco.clear()
        self.tx_Assunto.clear()
        self.tx_Telefone.clear()
        self.tx_Observacao.clear()
        self.cb_Departamento.setCurrentIndex(0)
     

        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Agendamento()
    system.show()
    sys.exit(app.exec())