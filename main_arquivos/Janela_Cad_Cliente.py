from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from Form_Cad_Clientes import Ui_Form_Cad_Clientes
from banco import Classe_Banco


class Classe_Cad_Cliente(QMainWindow):
    def __init__(self):
        super().__init__()
        self.janela_cad_clientes = Ui_Form_Cad_Clientes()
        self.janela_cad_clientes.setupUi(self)
        self.janela_banco = Classe_Banco()
        self.janela_cad_clientes.Bt_Salvar.clicked.connect(self.cadastrar_usuario)
        self.janela_cad_clientes.Bt_Voltar.clicked.connect(self.sair_cad_clientes)


    def cadastrar_usuario(self):
        self.janela_banco.cadastrar()
        nome = self.janela_cad_clientes.tx_Nome.text()
        cpf = self.janela_cad_clientes.tx_cpf.text()
        rg = self.janela_cad_clientes.tx_rg.text()
        telefone = self.janela_cad_clientes.tx_Telefone.text()
        email = self.janela_cad_clientes.tx_Email.text()
        cep = self.janela_cad_clientes.tx_Cep.text()
        endereco = self.janela_cad_clientes.tx_Endereco.text()
        numero = self.janela_cad_clientes.tx_Numero.text()
        bairro = self.janela_cad_clientes.tx_Bairro.text()
        cidade = self.janela_cad_clientes.tx_Cidade.text()
        estado = self.janela_cad_clientes.tx_Estado.text()
        if nome == "":
            self.alt_cad_em_branco()
        elif cpf == "":
                self.alt_cad_em_branco()
        elif telefone == "":
                self.alt_cad_em_branco()
        else:
            self.janela_banco.cursorr.execute("INSERT INTO pdv.clientes (nome,cpf,rg,telefone,email,cep,endereco,numero,bairro,cidade,estado) VALUES('"+nome+"','"+cpf+"','"+rg+"','"+telefone+"','"+email+"','"+cep+"','"+endereco+"','"+numero+"','"+bairro+"','"+cidade+"','"+estado+"')")
            self.janela_banco.banco.commit()
            self.janela_banco.banco.close()
            self.alt_cadastro_sucesso()


    def sair_cad_clientes(self):
        self.janela_cad_clientes.tx_Nome.clear()
        self.janela_cad_clientes.tx_cpf.clear()
        self.janela_cad_clientes.tx_rg.clear()
        self.janela_cad_clientes.tx_Telefone.clear()
        self.janela_cad_clientes.tx_Email.clear()
        self.janela_cad_clientes.tx_Cep.clear()
        self.janela_cad_clientes.tx_Endereco.clear()
        self.janela_cad_clientes.tx_Numero.clear()
        self.janela_cad_clientes.tx_Bairro.clear()
        self.janela_cad_clientes.tx_Cidade.clear()
        self.janela_cad_clientes.tx_Estado.clear()
        self.close()


    def alt_cad_em_branco(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Complete os campos, nome, cpf e rg!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()


    def alt_cadastro_sucesso(self):
        msg = QMessageBox()
        msg.setWindowTitle("Parabéns!")
        msg.setText("Cliente Cadastrado Com Sucesso!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()
        self.janela_cad_clientes.tx_Nome.clear()
        self.janela_cad_clientes.tx_cpf.clear()
        self.janela_cad_clientes.tx_rg.clear()        
        self.janela_cad_clientes.tx_Telefone.clear()
        self.janela_cad_clientes.tx_Email.clear()
        self.janela_cad_clientes.tx_Cep.clear() 
        self.janela_cad_clientes.tx_Endereco.clear()
        self.janela_cad_clientes.tx_Numero.clear()
        self.janela_cad_clientes.tx_Bairro.clear()
        self.janela_cad_clientes.tx_Cidade.clear()
        self.janela_cad_clientes.tx_Estado.clear()


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    window = Classe_Cad_Cliente()
    window.show()
    (app.exec())