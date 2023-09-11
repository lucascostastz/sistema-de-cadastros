from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtWidgets
import sys
from Form_Inicio import Ui_Form_Inicio
from Janela_Cad_Cliente import Classe_Cad_Cliente
from Janela_Cad_Produto import Classe_Cad_Produto
from Janela_Cad_Usuario import Classe_Cad_Usuario
from Janela_Edit_Usuario import Classe_Edit_Usuario
from banco import Classe_Banco


class Classe_Inicio(QMainWindow):
    def __init__(self):
        super(Classe_Inicio).__init__()
        self.janela_inicio = Ui_Form_Inicio()
        self.janela_inicio.setupUi(self)
        self.jan_cad_cliente = Classe_Cad_Cliente()
        self.jan_cad_produto = Classe_Cad_Produto()
        self.jan_cad_usuario = Classe_Cad_Usuario()
        self.jan_edit_usuario = Classe_Edit_Usuario()
        self.janela_banco = Classe_Banco()

        self.janela_inicio.Bt_Cad_Cliente.clicked.connect(self.chama_cad_cliente)
        self.janela_inicio.Bt_Add_Produto.clicked.connect(self.chama_cad_produto)
        self.janela_inicio.Bt_Add_Usuario.clicked.connect(self.chama_cad_usuario)
        self.janela_inicio.Bt_Edit_Usuario.clicked.connect(self.editar_usuario)

        self.janela_inicio.Bt_Inicio.clicked.connect(
        lambda: self.janela_inicio.stackedWidget.setCurrentWidget(self.tela_inicio()))
        self.tela_inicio()

    def tela_inicio(self):
        self.janela_inicio.Bt_Inicio.clicked.connect(
        lambda: self.janela_inicio.stackedWidget.setCurrentWidget(self.janela_inicio.inicio))


        self.janela_inicio.Bt_Clientes.clicked.connect(
        lambda: self.janela_inicio.stackedWidget.setCurrentWidget(self.tela_clientes()))
        self.tela_clientes()

    def tela_clientes(self):
        self.janela_inicio.Bt_Clientes.clicked.connect(
        lambda: self.janela_inicio.stackedWidget.setCurrentWidget(self.janela_inicio.clientes))


        self.janela_inicio.Bt_Produtos.clicked.connect(
        lambda: self.janela_inicio.stackedWidget.setCurrentWidget(self.tela_produtos()))
        self.tela_produtos()

    def tela_produtos(self):
        self.janela_inicio.Bt_Produtos.clicked.connect(
        lambda: self.janela_inicio.stackedWidget.setCurrentWidget(self.janela_inicio.produtos))

    
        self.janela_inicio.Bt_Vendas.clicked.connect(
        lambda: self.janela_inicio.stackedWidget.setCurrentWidget(self.tela_vendas()))
        self.tela_vendas()

    def tela_vendas(self):
        self.janela_inicio.Bt_Vendas.clicked.connect(
        lambda: self.janela_inicio.stackedWidget.setCurrentWidget(self.janela_inicio.vendas))


        self.janela_inicio.Bt_Usuarios.clicked.connect(
        lambda: self.janela_inicio.stackedWidget.setCurrentWidget(self.tela_usuarios()))
        self.tela_usuarios()

    def tela_usuarios(self):
        self.janela_inicio.Bt_Usuarios.clicked.connect(
        lambda: self.janela_inicio.stackedWidget.setCurrentWidget(self.janela_inicio.usuarios))
        self.listar_usuarios()


    def chama_cad_cliente(self):
        self.jan_cad_cliente.show()


    def chama_cad_produto(self):
        self.jan_cad_produto.show()

    def chama_cad_usuario(self):
        self.jan_cad_usuario.show()


    def listar_usuarios(self):
        self.janela_inicio.TableWidget_Usuario.verticalHeader().hide()
        self.janela_banco.conectar()
        
        self.janela_banco.cursorr.execute("SELECT idusuarios, nome, login, nivel_de_acesso, permissao FROM pdv.usuarios")
        dados_lidos = self.janela_banco.cursorr.fetchall()
        self.janela_inicio.TableWidget_Usuario.setRowCount(len(dados_lidos))
        self.janela_inicio.TableWidget_Usuario.setColumnCount(5)
        for a in range(0, len(dados_lidos)):
            for b in range(0,5):
                self.janela_inicio.TableWidget_Usuario.setItem(
                    a, b, QtWidgets.QTableWidgetItem(str(dados_lidos[a][b])))
                

    def editar_usuario(self):
        linha = self.janela_inicio.TableWidget_Usuario.currentRow()
        self.janela_banco.conectar() 
        self.janela_banco.cursorr.execute("SELECT idusuarios FROM pdv.usuarios")
        self.dados_lidos = self.janela_banco.cursorr.fetchall()
        self.valor_id = self.dados_lidos[linha][0]
        self.janela_banco.cursorr.execute("SELECT * FROM pdv.usuarios WHERE idusuarios=" + str(self.valor_id))
        cliente = self.janela_banco.cursorr.fetchall()
        self.jan_edit_usuario.show()
        self.numero_id = self.valor_id
        self.jan_edit_usuario.janela_edit_usuario.tx_nome.setText(str(cliente[0][1]))
        self.jan_edit_usuario.janela_edit_usuario.tx_Login.setText(str(cliente[0][2]))
        self.jan_edit_usuario.janela_edit_usuario.cb_Nivel_Acesso.setCurrentText(str(cliente[0][5]))
        self.jan_edit_usuario.janela_edit_usuario.cb_Permissoes.setCurrentText(str(cliente[0][6]))


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    Iniciar = Classe_Inicio()
    Iniciar.show()
    (app.exec())