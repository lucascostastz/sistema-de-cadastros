# Form implementation generated from reading ui file 'Form_Cad_Clientes.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_Cad_Clientes(object):
    def setupUi(self, Form_Cad_Clientes):
        Form_Cad_Clientes.setObjectName("Form_Cad_Clientes")
        Form_Cad_Clientes.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Form_Cad_Clientes.resize(700, 435)
        Form_Cad_Clientes.setMinimumSize(QtCore.QSize(700, 435))
        Form_Cad_Clientes.setMaximumSize(QtCore.QSize(700, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../img/clientes.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form_Cad_Clientes.setWindowIcon(icon)
        self.fr_FormClientes = QtWidgets.QFrame(parent=Form_Cad_Clientes)
        self.fr_FormClientes.setGeometry(QtCore.QRect(0, 0, 700, 400))
        self.fr_FormClientes.setMinimumSize(QtCore.QSize(700, 400))
        self.fr_FormClientes.setMaximumSize(QtCore.QSize(700, 350))
        self.fr_FormClientes.setStyleSheet("background: #FFF;\n"
"border: none")
        self.fr_FormClientes.setObjectName("fr_FormClientes")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.fr_FormClientes)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tx_Nome = QtWidgets.QLineEdit(parent=self.fr_FormClientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tx_Nome.sizePolicy().hasHeightForWidth())
        self.tx_Nome.setSizePolicy(sizePolicy)
        self.tx_Nome.setMinimumSize(QtCore.QSize(0, 25))
        self.tx_Nome.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tx_Nome.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.tx_Nome.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Nome.setObjectName("tx_Nome")
        self.gridLayout_3.addWidget(self.tx_Nome, 2, 0, 1, 3)
        self.lb_Descricao = QtWidgets.QLabel(parent=self.fr_FormClientes)
        self.lb_Descricao.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_Descricao.setObjectName("lb_Descricao")
        self.gridLayout_3.addWidget(self.lb_Descricao, 0, 1, 1, 2)
        self.lb_FormTelefone = QtWidgets.QLabel(parent=self.fr_FormClientes)
        self.lb_FormTelefone.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormTelefone.setObjectName("lb_FormTelefone")
        self.gridLayout_3.addWidget(self.lb_FormTelefone, 3, 2, 1, 1)
        self.lb_FormCpf = QtWidgets.QLabel(parent=self.fr_FormClientes)
        self.lb_FormCpf.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormCpf.setObjectName("lb_FormCpf")
        self.gridLayout_3.addWidget(self.lb_FormCpf, 3, 0, 1, 2)
        self.tx_cpf = QtWidgets.QLineEdit(parent=self.fr_FormClientes)
        self.tx_cpf.setMinimumSize(QtCore.QSize(300, 30))
        self.tx_cpf.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.tx_cpf.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_cpf.setPlaceholderText("")
        self.tx_cpf.setObjectName("tx_cpf")
        self.gridLayout_3.addWidget(self.tx_cpf, 4, 0, 1, 2)
        self.label = QtWidgets.QLabel(parent=self.fr_FormClientes)
        self.label.setMaximumSize(QtCore.QSize(35, 25))
        self.label.setStyleSheet("background: #CFCFCF;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.lb_FormNome = QtWidgets.QLabel(parent=self.fr_FormClientes)
        self.lb_FormNome.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormNome.setObjectName("lb_FormNome")
        self.gridLayout_3.addWidget(self.lb_FormNome, 1, 0, 1, 2)
        self.tx_Telefone = QtWidgets.QLineEdit(parent=self.fr_FormClientes)
        self.tx_Telefone.setMinimumSize(QtCore.QSize(300, 30))
        self.tx_Telefone.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.tx_Telefone.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Telefone.setMaxLength(15)
        self.tx_Telefone.setCursorPosition(15)
        self.tx_Telefone.setPlaceholderText("")
        self.tx_Telefone.setObjectName("tx_Telefone")
        self.gridLayout_3.addWidget(self.tx_Telefone, 4, 2, 1, 1)
        self.lb_Linha = QtWidgets.QLabel(parent=self.fr_FormClientes)
        self.lb_Linha.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: normal;\n"
"\n"
"border-bottom: 2px solid #A2A2A2;\n"
"color: #797979\n"
"}")
        self.lb_Linha.setText("")
        self.lb_Linha.setObjectName("lb_Linha")
        self.gridLayout_3.addWidget(self.lb_Linha, 5, 0, 1, 3)
        self.lb_DescrecaoEndereco = QtWidgets.QLabel(parent=self.fr_FormClientes)
        self.lb_DescrecaoEndereco.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_DescrecaoEndereco.setObjectName("lb_DescrecaoEndereco")
        self.gridLayout_3.addWidget(self.lb_DescrecaoEndereco, 6, 0, 1, 2)
        self.tx_Endereco = QtWidgets.QLineEdit(parent=self.fr_FormClientes)
        self.tx_Endereco.setMinimumSize(QtCore.QSize(0, 30))
        self.tx_Endereco.setMaximumSize(QtCore.QSize(16777215, 25))
        self.tx_Endereco.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.tx_Endereco.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Endereco.setInputMask("")
        self.tx_Endereco.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tx_Endereco.setObjectName("tx_Endereco")
        self.gridLayout_3.addWidget(self.tx_Endereco, 7, 0, 1, 3)
        self.fr_Botoes = QtWidgets.QFrame(parent=Form_Cad_Clientes)
        self.fr_Botoes.setGeometry(QtCore.QRect(0, 400, 700, 35))
        self.fr_Botoes.setMinimumSize(QtCore.QSize(150, 35))
        self.fr_Botoes.setMaximumSize(QtCore.QSize(700, 35))
        self.fr_Botoes.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border:none;\n"
"\n"
"")
        self.fr_Botoes.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fr_Botoes.setObjectName("fr_Botoes")
        self.Bt_Salvar = QtWidgets.QPushButton(parent=self.fr_Botoes)
        self.Bt_Salvar.setGeometry(QtCore.QRect(540, 2, 70, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_Salvar.sizePolicy().hasHeightForWidth())
        self.Bt_Salvar.setSizePolicy(sizePolicy)
        self.Bt_Salvar.setMinimumSize(QtCore.QSize(70, 30))
        self.Bt_Salvar.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Bt_Salvar.setFont(font)
        self.Bt_Salvar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Bt_Salvar.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Bt_Salvar.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.Bt_Salvar.setStyleSheet("QPushButton {\n"
"background-color: #7AB32E;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/salvar/salvar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Bt_Salvar.setIcon(icon1)
        self.Bt_Salvar.setIconSize(QtCore.QSize(50, 25))
        self.Bt_Salvar.setObjectName("Bt_Salvar")
        self.Bt_Voltar = QtWidgets.QPushButton(parent=self.fr_Botoes)
        self.Bt_Voltar.setGeometry(QtCore.QRect(620, 2, 70, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_Voltar.sizePolicy().hasHeightForWidth())
        self.Bt_Voltar.setSizePolicy(sizePolicy)
        self.Bt_Voltar.setMinimumSize(QtCore.QSize(70, 30))
        self.Bt_Voltar.setMaximumSize(QtCore.QSize(70, 25))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Bt_Voltar.setFont(font)
        self.Bt_Voltar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Bt_Voltar.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Bt_Voltar.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.Bt_Voltar.setStyleSheet("QPushButton {\n"
"background-color: #7AB32E;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/sair/delete_delete_exit_1577.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Bt_Voltar.setIcon(icon2)
        self.Bt_Voltar.setIconSize(QtCore.QSize(75, 25))
        self.Bt_Voltar.setObjectName("Bt_Voltar")

        self.retranslateUi(Form_Cad_Clientes)
        QtCore.QMetaObject.connectSlotsByName(Form_Cad_Clientes)
        Form_Cad_Clientes.setTabOrder(self.tx_Nome, self.tx_cpf)
        Form_Cad_Clientes.setTabOrder(self.tx_cpf, self.tx_Telefone)
        Form_Cad_Clientes.setTabOrder(self.tx_Telefone, self.tx_Endereco)

    def retranslateUi(self, Form_Cad_Clientes):
        _translate = QtCore.QCoreApplication.translate
        Form_Cad_Clientes.setWindowTitle(_translate("Form_Cad_Clientes", "LC INFORMÁTICA| CADASTRAR CLIENTE"))
        self.tx_Nome.setPlaceholderText(_translate("Form_Cad_Clientes", "NOME COMPLETO"))
        self.lb_Descricao.setText(_translate("Form_Cad_Clientes", "FICHA CADASTRAL CLIENTE"))
        self.lb_FormTelefone.setText(_translate("Form_Cad_Clientes", "TELEFONE"))
        self.lb_FormCpf.setText(_translate("Form_Cad_Clientes", "CPF"))
        self.tx_cpf.setInputMask(_translate("Form_Cad_Clientes", "000.000.000-00"))
        self.tx_cpf.setText(_translate("Form_Cad_Clientes", "..-"))
        self.lb_FormNome.setText(_translate("Form_Cad_Clientes", "NOME"))
        self.tx_Telefone.setInputMask(_translate("Form_Cad_Clientes", "(00) 0000-00000"))
        self.tx_Telefone.setText(_translate("Form_Cad_Clientes", "() -"))
        self.lb_DescrecaoEndereco.setText(_translate("Form_Cad_Clientes", "ENDEREÇO"))
        self.tx_Endereco.setPlaceholderText(_translate("Form_Cad_Clientes", "Endereço ou localidade"))
        self.Bt_Salvar.setText(_translate("Form_Cad_Clientes", "SALVAR"))
        self.Bt_Voltar.setText(_translate("Form_Cad_Clientes", "SAIR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Cad_Clientes = QtWidgets.QFrame()
    ui = Ui_Form_Cad_Clientes()
    ui.setupUi(Form_Cad_Clientes)
    Form_Cad_Clientes.show()
    sys.exit(app.exec())
