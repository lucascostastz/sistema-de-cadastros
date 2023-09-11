# Form implementation generated from reading ui file 'Form_Edit_Usuario.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_Edit_Usuario(object):
    def setupUi(self, Form_Edit_Usuario):
        Form_Edit_Usuario.setObjectName("Form_Edit_Usuario")
        Form_Edit_Usuario.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Form_Edit_Usuario.resize(800, 470)
        Form_Edit_Usuario.setMinimumSize(QtCore.QSize(800, 470))
        Form_Edit_Usuario.setMaximumSize(QtCore.QSize(800, 470))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../img/edit-.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form_Edit_Usuario.setWindowIcon(icon)
        self.fr_FormProdutos = QtWidgets.QFrame(parent=Form_Edit_Usuario)
        self.fr_FormProdutos.setGeometry(QtCore.QRect(0, -1, 1000, 531))
        self.fr_FormProdutos.setStyleSheet("background: #FFF;\n"
"border: none")
        self.fr_FormProdutos.setObjectName("fr_FormProdutos")
        self.lb_FormProdutos = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos.setGeometry(QtCore.QRect(19, 10, 961, 30))
        self.lb_FormProdutos.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"    color: rgb(0, 170, 255);\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormProdutos.setObjectName("lb_FormProdutos")
        self.tx_idProduto = QtWidgets.QLineEdit(parent=self.fr_FormProdutos)
        self.tx_idProduto.setEnabled(False)
        self.tx_idProduto.setGeometry(QtCore.QRect(20, 170, 150, 25))
        self.tx_idProduto.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border: 1px solid #A2A2A2;\n"
"color: #000;\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"}")
        self.tx_idProduto.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tx_idProduto.setObjectName("tx_idProduto")
        self.lb_FotoProduto = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FotoProduto.setGeometry(QtCore.QRect(20, 70, 241, 271))
        self.lb_FotoProduto.setStyleSheet("border: 1px solid #A2A2A2;\n"
"\n"
"")
        self.lb_FotoProduto.setText("")
        self.lb_FotoProduto.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_FotoProduto.setObjectName("lb_FotoProduto")
        self.lb_FormProdutos_2 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos_2.setGeometry(QtCore.QRect(280, 60, 150, 20))
        self.lb_FormProdutos_2.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_2.setObjectName("lb_FormProdutos_2")
        self.tx_nome = QtWidgets.QLineEdit(parent=self.fr_FormProdutos)
        self.tx_nome.setGeometry(QtCore.QRect(280, 85, 450, 25))
        self.tx_nome.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.tx_nome.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_nome.setObjectName("tx_nome")
        self.lb_FormProdutos_3 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos_3.setGeometry(QtCore.QRect(280, 290, 111, 20))
        self.lb_FormProdutos_3.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_3.setObjectName("lb_FormProdutos_3")
        self.cb_Nivel_Acesso = QtWidgets.QComboBox(parent=self.fr_FormProdutos)
        self.cb_Nivel_Acesso.setGeometry(QtCore.QRect(280, 320, 221, 25))
        self.cb_Nivel_Acesso.setStyleSheet("QComboBox{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QComboBox:Focus {\n"
"border: 1px solid red;\n"
"}\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 25px;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"QComboBox::down-arrow {\n"
"     image: url(\"+self.resourcepath(\'Images/down.png\')+\");\n"
" }\n"
"")
        self.cb_Nivel_Acesso.setObjectName("cb_Nivel_Acesso")
        self.cb_Nivel_Acesso.addItem("")
        self.cb_Nivel_Acesso.addItem("")
        self.cb_Nivel_Acesso.addItem("")
        self.bt_AddCategoriaProduto = QtWidgets.QPushButton(parent=self.fr_FormProdutos)
        self.bt_AddCategoriaProduto.setGeometry(QtCore.QRect(480, 320, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_AddCategoriaProduto.setFont(font)
        self.bt_AddCategoriaProduto.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_AddCategoriaProduto.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/add/Sem.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_AddCategoriaProduto.setIcon(icon1)
        self.bt_AddCategoriaProduto.setObjectName("bt_AddCategoriaProduto")
        self.lb_FormProdutos_4 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos_4.setGeometry(QtCore.QRect(580, 290, 81, 20))
        self.lb_FormProdutos_4.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_4.setObjectName("lb_FormProdutos_4")
        self.cb_Permissoes = QtWidgets.QComboBox(parent=self.fr_FormProdutos)
        self.cb_Permissoes.setGeometry(QtCore.QRect(520, 320, 211, 25))
        self.cb_Permissoes.setStyleSheet("QComboBox{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QComboBox:Focus {\n"
"border: 1px solid red;\n"
"}\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 25px;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"QComboBox::down-arrow {\n"
"     image: url(\"+self.resourcepath(\'Images/down.png\')+\");\n"
" }\n"
"")
        self.cb_Permissoes.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAtBottom)
        self.cb_Permissoes.setFrame(False)
        self.cb_Permissoes.setObjectName("cb_Permissoes")
        self.cb_Permissoes.addItem("")
        self.cb_Permissoes.addItem("")
        self.cb_Permissoes.addItem("")
        self.bt_AddMarcaProduto = QtWidgets.QPushButton(parent=self.fr_FormProdutos)
        self.bt_AddMarcaProduto.setGeometry(QtCore.QRect(710, 320, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_AddMarcaProduto.setFont(font)
        self.bt_AddMarcaProduto.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_AddMarcaProduto.setText("")
        self.bt_AddMarcaProduto.setIcon(icon1)
        self.bt_AddMarcaProduto.setObjectName("bt_AddMarcaProduto")
        self.lb_FormProdutos_8 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos_8.setGeometry(QtCore.QRect(20, 350, 960, 30))
        self.lb_FormProdutos_8.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: normal;\n"
"\n"
"border-bottom: 2px solid #A2A2A2;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_8.setText("")
        self.lb_FormProdutos_8.setObjectName("lb_FormProdutos_8")
        self.fr_BotoesFormProdutos = QtWidgets.QFrame(parent=self.fr_FormProdutos)
        self.fr_BotoesFormProdutos.setGeometry(QtCore.QRect(0, 470, 1000, 30))
        self.fr_BotoesFormProdutos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none;")
        self.fr_BotoesFormProdutos.setObjectName("fr_BotoesFormProdutos")
        self.lb_qtdeMin = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_qtdeMin.setGeometry(QtCore.QRect(890, 350, 40, 35))
        self.lb_qtdeMin.setText("")
        self.lb_qtdeMin.setObjectName("lb_qtdeMin")
        self.tx_PorcentagemVarejo = QtWidgets.QLineEdit(parent=self.fr_FormProdutos)
        self.tx_PorcentagemVarejo.setGeometry(QtCore.QRect(360, 360, 60, 30))
        self.tx_PorcentagemVarejo.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.tx_PorcentagemVarejo.setStyleSheet("QLineEdit{\n"
"background: #FFF;\n"
"border-radius: 2px;\n"
"color: #7AB32E;\n"
"font: 20px \"Arial\" ;\n"
"font-weight: bold\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_PorcentagemVarejo.setText("")
        self.tx_PorcentagemVarejo.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tx_PorcentagemVarejo.setReadOnly(True)
        self.tx_PorcentagemVarejo.setObjectName("tx_PorcentagemVarejo")
        self.tx_PorcentagemAtacado = QtWidgets.QLineEdit(parent=self.fr_FormProdutos)
        self.tx_PorcentagemAtacado.setGeometry(QtCore.QRect(360, 420, 60, 30))
        self.tx_PorcentagemAtacado.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.tx_PorcentagemAtacado.setStyleSheet("QLineEdit{\n"
"background: #FFF;\n"
"border-radius: 2px;\n"
"color: #7AB32E;\n"
"font: 20px \"Arial\" ;\n"
"font-weight: bold\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_PorcentagemAtacado.setText("")
        self.tx_PorcentagemAtacado.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tx_PorcentagemAtacado.setReadOnly(True)
        self.tx_PorcentagemAtacado.setObjectName("tx_PorcentagemAtacado")
        self.Bt_CancelAddCatergoria = QtWidgets.QPushButton(parent=self.fr_FormProdutos)
        self.Bt_CancelAddCatergoria.setGeometry(QtCore.QRect(390, 320, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Bt_CancelAddCatergoria.setFont(font)
        self.Bt_CancelAddCatergoria.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.Bt_CancelAddCatergoria.setText("")
        self.Bt_CancelAddCatergoria.setObjectName("Bt_CancelAddCatergoria")
        self.lb_FormProdutos_5 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos_5.setGeometry(QtCore.QRect(280, 130, 150, 20))
        self.lb_FormProdutos_5.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_5.setObjectName("lb_FormProdutos_5")
        self.tx_Login = QtWidgets.QLineEdit(parent=self.fr_FormProdutos)
        self.tx_Login.setGeometry(QtCore.QRect(280, 160, 450, 25))
        self.tx_Login.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.tx_Login.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Login.setObjectName("tx_Login")
        self.lb_FormProdutos_6 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos_6.setGeometry(QtCore.QRect(280, 210, 150, 20))
        self.lb_FormProdutos_6.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_6.setObjectName("lb_FormProdutos_6")
        self.tx_Senha = QtWidgets.QLineEdit(parent=self.fr_FormProdutos)
        self.tx_Senha.setGeometry(QtCore.QRect(280, 240, 221, 25))
        self.tx_Senha.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.tx_Senha.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.tx_Senha.setObjectName("tx_Senha")
        self.lb_FormProdutos_9 = QtWidgets.QLabel(parent=self.fr_FormProdutos)
        self.lb_FormProdutos_9.setGeometry(QtCore.QRect(570, 210, 150, 20))
        self.lb_FormProdutos_9.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_9.setObjectName("lb_FormProdutos_9")
        self.tx_Senha2 = QtWidgets.QLineEdit(parent=self.fr_FormProdutos)
        self.tx_Senha2.setGeometry(QtCore.QRect(520, 240, 211, 25))
        self.tx_Senha2.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.tx_Senha2.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Senha2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.tx_Senha2.setObjectName("tx_Senha2")
        self.pushButton = QtWidgets.QPushButton(parent=self.fr_FormProdutos)
        self.pushButton.setGeometry(QtCore.QRect(40, 170, 191, 51))
        self.pushButton.setObjectName("pushButton")
        self.bt_SalvarUsuario = QtWidgets.QPushButton(parent=self.fr_FormProdutos)
        self.bt_SalvarUsuario.setGeometry(QtCore.QRect(510, 440, 91, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_SalvarUsuario.setFont(font)
        self.bt_SalvarUsuario.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_SalvarUsuario.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.bt_SalvarUsuario.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.bt_SalvarUsuario.setStyleSheet("QPushButton {\n"
"background-color: #7AB32E;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/salvar/salvar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_SalvarUsuario.setIcon(icon2)
        self.bt_SalvarUsuario.setIconSize(QtCore.QSize(50, 25))
        self.bt_SalvarUsuario.setObjectName("bt_SalvarUsuario")
        self.Bt_CancelarUsuario = QtWidgets.QPushButton(parent=self.fr_FormProdutos)
        self.Bt_CancelarUsuario.setGeometry(QtCore.QRect(630, 440, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Bt_CancelarUsuario.setFont(font)
        self.Bt_CancelarUsuario.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Bt_CancelarUsuario.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Bt_CancelarUsuario.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.Bt_CancelarUsuario.setStyleSheet("QPushButton {\n"
"background-color: #1E87F0;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/sair/delete_delete_exit_1577.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Bt_CancelarUsuario.setIcon(icon3)
        self.Bt_CancelarUsuario.setIconSize(QtCore.QSize(75, 25))
        self.Bt_CancelarUsuario.setObjectName("Bt_CancelarUsuario")
        self.Bt_CancelAddCatergoria.raise_()
        self.lb_FormProdutos.raise_()
        self.tx_idProduto.raise_()
        self.lb_FotoProduto.raise_()
        self.lb_FormProdutos_2.raise_()
        self.tx_nome.raise_()
        self.lb_FormProdutos_3.raise_()
        self.cb_Nivel_Acesso.raise_()
        self.bt_AddCategoriaProduto.raise_()
        self.lb_FormProdutos_4.raise_()
        self.cb_Permissoes.raise_()
        self.bt_AddMarcaProduto.raise_()
        self.lb_FormProdutos_8.raise_()
        self.fr_BotoesFormProdutos.raise_()
        self.lb_qtdeMin.raise_()
        self.tx_PorcentagemVarejo.raise_()
        self.tx_PorcentagemAtacado.raise_()
        self.lb_FormProdutos_5.raise_()
        self.tx_Login.raise_()
        self.lb_FormProdutos_6.raise_()
        self.tx_Senha.raise_()
        self.lb_FormProdutos_9.raise_()
        self.tx_Senha2.raise_()
        self.pushButton.raise_()
        self.bt_SalvarUsuario.raise_()
        self.Bt_CancelarUsuario.raise_()

        self.retranslateUi(Form_Edit_Usuario)
        QtCore.QMetaObject.connectSlotsByName(Form_Edit_Usuario)
        Form_Edit_Usuario.setTabOrder(self.tx_nome, self.tx_Login)
        Form_Edit_Usuario.setTabOrder(self.tx_Login, self.tx_Senha)
        Form_Edit_Usuario.setTabOrder(self.tx_Senha, self.tx_Senha2)
        Form_Edit_Usuario.setTabOrder(self.tx_Senha2, self.cb_Nivel_Acesso)
        Form_Edit_Usuario.setTabOrder(self.cb_Nivel_Acesso, self.bt_AddMarcaProduto)
        Form_Edit_Usuario.setTabOrder(self.bt_AddMarcaProduto, self.tx_PorcentagemVarejo)
        Form_Edit_Usuario.setTabOrder(self.tx_PorcentagemVarejo, self.tx_PorcentagemAtacado)
        Form_Edit_Usuario.setTabOrder(self.tx_PorcentagemAtacado, self.Bt_CancelAddCatergoria)
        Form_Edit_Usuario.setTabOrder(self.Bt_CancelAddCatergoria, self.tx_idProduto)
        Form_Edit_Usuario.setTabOrder(self.tx_idProduto, self.cb_Permissoes)
        Form_Edit_Usuario.setTabOrder(self.cb_Permissoes, self.bt_AddCategoriaProduto)
        Form_Edit_Usuario.setTabOrder(self.bt_AddCategoriaProduto, self.pushButton)

    def retranslateUi(self, Form_Edit_Usuario):
        _translate = QtCore.QCoreApplication.translate
        Form_Edit_Usuario.setWindowTitle(_translate("Form_Edit_Usuario", "LC INFORMÁTICA | EDITAR USUÁRIOS"))
        self.lb_FormProdutos.setText(_translate("Form_Edit_Usuario", "EDITAR USUÁRIO"))
        self.tx_idProduto.setText(_translate("Form_Edit_Usuario", "selecione uma foto"))
        self.lb_FormProdutos_2.setText(_translate("Form_Edit_Usuario", "NOME COMPLETO"))
        self.tx_nome.setPlaceholderText(_translate("Form_Edit_Usuario", "DIGITE SEU NOME"))
        self.lb_FormProdutos_3.setText(_translate("Form_Edit_Usuario", "NÍVEL DE ACESSO"))
        self.cb_Nivel_Acesso.setItemText(0, _translate("Form_Edit_Usuario", "SELECIONE"))
        self.cb_Nivel_Acesso.setItemText(1, _translate("Form_Edit_Usuario", "ADMINISTRADOR"))
        self.cb_Nivel_Acesso.setItemText(2, _translate("Form_Edit_Usuario", "USUÁRIO"))
        self.lb_FormProdutos_4.setText(_translate("Form_Edit_Usuario", "PERMISSÕES"))
        self.cb_Permissoes.setItemText(0, _translate("Form_Edit_Usuario", "SELECIONE"))
        self.cb_Permissoes.setItemText(1, _translate("Form_Edit_Usuario", "VISUALIZAR"))
        self.cb_Permissoes.setItemText(2, _translate("Form_Edit_Usuario", "ALTERAR"))
        self.Bt_CancelAddCatergoria.setToolTip(_translate("Form_Edit_Usuario", "<html><head/><body><p>Cancelar</p></body></html>"))
        self.lb_FormProdutos_5.setText(_translate("Form_Edit_Usuario", "NOME DE USUÁRIO"))
        self.tx_Login.setPlaceholderText(_translate("Form_Edit_Usuario", "DIGiTE SEU LOGIN"))
        self.lb_FormProdutos_6.setText(_translate("Form_Edit_Usuario", "SENHA"))
        self.tx_Senha.setPlaceholderText(_translate("Form_Edit_Usuario", "DIGITE SUA SENHA"))
        self.lb_FormProdutos_9.setText(_translate("Form_Edit_Usuario", "REPITA A SENHA"))
        self.tx_Senha2.setPlaceholderText(_translate("Form_Edit_Usuario", "DIGITE A SENHA NOVAMENTE"))
        self.pushButton.setText(_translate("Form_Edit_Usuario", "Selecione uma foto"))
        self.bt_SalvarUsuario.setText(_translate("Form_Edit_Usuario", "SALVAR"))
        self.Bt_CancelarUsuario.setText(_translate("Form_Edit_Usuario", "CANCELAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Edit_Usuario = QtWidgets.QFrame()
    ui = Ui_Form_Edit_Usuario()
    ui.setupUi(Form_Edit_Usuario)
    Form_Edit_Usuario.show()
    sys.exit(app.exec())
