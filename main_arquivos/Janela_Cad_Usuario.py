from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from Form_Cad_Usuario import Ui_Form_Cad_Usuario
from banco import Classe_Banco


class Classe_Cad_Usuario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.janela_cad_usuario = Ui_Form_Cad_Usuario()
        self.janela_cad_usuario.setupUi(self)
        self.janela_banco = Classe_Banco()

        self.janela_cad_usuario.bt_SalvarUsuario.clicked.connect(self.cadastrar_usuario)
        self.janela_cad_usuario.Bt_CancelarUsuario.clicked.connect(self.sair_cad_usuario)


    def cadastrar_usuario(self):
        self.janela_banco.cadastrar()
        nome = self.janela_cad_usuario.tx_nome.text()
        login = self.janela_cad_usuario.tx_Login.text()
        senha_login_1 = self.janela_cad_usuario.tx_Senha.text()
        senha_login_2 = self.janela_cad_usuario.tx_Senha2.text()
        nivel_acesso = self.janela_cad_usuario.cb_Nivel_Acesso.currentText()
        permissao = self.janela_cad_usuario.cb_Permissoes.currentText()
        if nome == "":
            self.alt_cad_em_branco()
        elif login == "":
                self.alt_cad_em_branco()
        elif senha_login_1 == "":
                self.alt_cad_em_branco()
        elif senha_login_2 == "":
                self.alt_cad_em_branco()
        elif nivel_acesso == "SELECIONE":
                self.alt_erro_cad_nivel_acesso()
        elif permissao == "SELECIONE":
                self.alt_erro_cad_permissao()
        elif senha_login_1 != senha_login_2:
                self.alt_senha_diferente()
        else:
            self.janela_banco.cursorr.execute("INSERT INTO pdv.usuarios (nome,login,senha1,senha2,nivel_de_acesso,permissao) VALUES('"+nome+"','"+
                    login+"','"+senha_login_1+"','"+senha_login_2+"','"+nivel_acesso+"','"+permissao+"')")
            self.janela_banco.banco.commit()
            self.janela_banco.banco.close()
            self.alt_cadastro_sucesso()


    def alt_erro_cad_nivel_acesso(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Selecione um Nível de Acesso do Usuário!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def alt_erro_cad_permissao(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Selecione as Permissões de Acesso do Usuário!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def alt_cad_em_branco(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("Complete os Campos em Branco!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def alt_senha_diferente(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta!")
        msg.setText("As Senhas Estão Diferentes!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def alt_cadastro_sucesso(self):
        msg = QMessageBox()
        msg.setWindowTitle("Parabéns!")
        msg.setText("Usuário Cadastrado Com Sucesso!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()
        self.janela_cad_usuario.tx_nome.clear()
        self.janela_cad_usuario.tx_Login.clear()
        self.janela_cad_usuario.tx_Senha.clear()
        self.janela_cad_usuario.tx_Senha2.clear()
        self.janela_cad_usuario.cb_Nivel_Acesso.setCurrentIndex(0)
        self.janela_cad_usuario.cb_Permissoes.setCurrentIndex(0)


    def sair_cad_usuario(self):
        self.janela_cad_usuario.tx_nome.clear()
        self.janela_cad_usuario.tx_Login.clear()
        self.janela_cad_usuario.tx_Senha.clear()
        self.janela_cad_usuario.tx_Senha2.clear()
        self.janela_cad_usuario.cb_Nivel_Acesso.setCurrentIndex(0)
        self.janela_cad_usuario.cb_Permissoes.setCurrentIndex(0)
        self.close()


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    window = Classe_Cad_Usuario()
    window.show()
    (app.exec())