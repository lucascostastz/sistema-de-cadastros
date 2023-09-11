from Form_Edit_Usuario import Ui_Form_Edit_Usuario
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from Janela_Inicio import Classe_Inicio


class Classe_Edit_Usuario(QMainWindow):
    def __init__(self):
        super(Classe_Edit_Usuario).__init__()
        self.janela_edit_usuario = Ui_Form_Edit_Usuario()
        self.janela_edit_usuario.setupUi(self)
        self.janela_edit_usuario.bt_SalvarUsuario.clicked.connect(self.salvar_usuario_editados)
  


    def salvar_usuario_editados(self):
        self.teste = Classe_Inicio()
        # Pega o numero id
        # Valor digitado no lineEdit
        nome = self.janela_edit_usuario.tx_nome.text()
        login = self.janela_edit_usuario.tx_Login.text()
        senha_login_1 = self.janela_edit_usuario.tx_Senha.text()
        senha_login_2 = self.janela_edit_usuario.tx_Senha2.text()
        nivel_acesso = self.janela_edit_usuario.cb_Nivel_Acesso.currentText()
        permissao = self.janela_edit_usuario.cb_Permissoes.currentText()
        # Atualizar os dados no banco
        self.janela_banco.conectar() 
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
            self.janela_banco.cursorr.execute("UPDATE saude.usuarios SET nome = '{}', login = '{}', senha1 = '{}', senha2 ='{}', nivel_de_acesso = '{}', permissao = '{}' WHERE idusuarios = {}".format(
                nome, login, senha_login_1, senha_login_2, nivel_acesso, permissao, self.jan_inicio.numero))
            self.janela_banco.banco.commit()
            self.alerta_user_edit()
            self.limpar_edit_user()

        
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


    def alerta_user_edit(self):
        msg = QMessageBox()
        msg.setWindowTitle("Parabéns!")
        msg.setText("Editado com Sucesso!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()


    def sair_edit_usuario(self):
        self.limpar_edit_user()
        self.close()
        

    def limpar_edit_user(self):
        self.janela_edit_usuario.tx_nome.clear()
        self.janela_edit_usuario.tx_Login.clear()
        self.janela_edit_usuario.tx_Senha.clear()
        self.janela_edit_usuario.cb_Nivel_Acesso.setCurrentIndex(0)
        self.janela_edit_usuario.cb_Permissoes.setCurrentIndex(0)
        self.close()