# Form implementation generated from reading ui file 'Form_Login.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_Login(object):
    def setupUi(self, Form_Login):
        Form_Login.setObjectName("Form_Login")
        Form_Login.resize(779, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_Login.sizePolicy().hasHeightForWidth())
        Form_Login.setSizePolicy(sizePolicy)
        Form_Login.setMinimumSize(QtCore.QSize(450, 450))
        Form_Login.setMaximumSize(QtCore.QSize(780, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../img/login-icon-3042.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form_Login.setWindowIcon(icon)
        Form_Login.setStyleSheet("color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=Form_Login)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Login = QtWidgets.QWidget()
        self.Login.setObjectName("Login")
        self.frame_4 = QtWidgets.QFrame(parent=self.Login)
        self.frame_4.setGeometry(QtCore.QRect(10, 0, 756, 432))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_4.setStyleSheet("background-color: rgb(94, 94, 94);\n"
"border: 0.5px solid black;\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_Main = QtWidgets.QWidget(parent=self.frame_4)
        self.widget_Main.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"")
        self.widget_Main.setObjectName("widget_Main")
        self.Lb_Background = QtWidgets.QLabel(parent=self.widget_Main)
        self.Lb_Background.setGeometry(QtCore.QRect(10, 10, 421, 361))
        self.Lb_Background.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0.518552, y1:0.414227, x2:0.52957, y2:1, stop:0 #00aaff, stop:1 rgb(47, 163, 163));\n"
"\n"
"border-top-left-radius:30px;\n"
"border-bottom-right-radius:30px;\n"
"\n"
"\n"
"\n"
"border:0px;\n"
"\n"
"\n"
"background-repeat: no-repeat;\n"
"\n"
" background-repeat: no-repeat;\n"
"background-position: center;\n"
"\n"
"")
        self.Lb_Background.setText("")
        self.Lb_Background.setPixmap(QtGui.QPixmap("../../WERWER.png"))
        self.Lb_Background.setScaledContents(True)
        self.Lb_Background.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Lb_Background.setObjectName("Lb_Background")
        self.Lb_background2 = QtWidgets.QLabel(parent=self.widget_Main)
        self.Lb_background2.setGeometry(QtCore.QRect(430, 10, 301, 361))
        self.Lb_background2.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"background-color: rgb(35, 35, 35);\n"
"\n"
"border-bottom-right-radius:20px;")
        self.Lb_background2.setText("")
        self.Lb_background2.setObjectName("Lb_background2")
        self.Tx_Usuario = QtWidgets.QLineEdit(parent=self.widget_Main)
        self.Tx_Usuario.setGeometry(QtCore.QRect(450, 150, 271, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tx_Usuario.sizePolicy().hasHeightForWidth())
        self.Tx_Usuario.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Tx_Usuario.setFont(font)
        self.Tx_Usuario.setStyleSheet("QLineEdit{\n"
"    color: rgb(0, 0, 0);\n"
"border:0px solid;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border-bottom:2px solid blue;\n"
"    background-color: rgb(238, 238, 236);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-bottom:2px solid rgb(238, 238, 236);\n"
"}\n"
"QLineEdit:focus {\n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"     border-bottom:2px solid rgb(238, 238, 236);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"\n"
"")
        self.Tx_Usuario.setText("")
        self.Tx_Usuario.setFrame(True)
        self.Tx_Usuario.setReadOnly(False)
        self.Tx_Usuario.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.Tx_Usuario.setClearButtonEnabled(True)
        self.Tx_Usuario.setObjectName("Tx_Usuario")
        self.Tx_Senha = QtWidgets.QLineEdit(parent=self.widget_Main)
        self.Tx_Senha.setGeometry(QtCore.QRect(450, 190, 271, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tx_Senha.sizePolicy().hasHeightForWidth())
        self.Tx_Senha.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Tx_Senha.setFont(font)
        self.Tx_Senha.setStyleSheet("QLineEdit{\n"
"    color: rgb(0, 0, 0);\n"
"border:0px solid;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border-bottom:2px solid blue;\n"
"    background-color: rgb(238, 238, 236);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-bottom:2px solid rgb(238, 238, 236);\n"
"}\n"
"QLineEdit:focus {\n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"     border-bottom:2px solid rgb(238, 238, 236);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"\n"
"")
        self.Tx_Senha.setText("")
        self.Tx_Senha.setFrame(False)
        self.Tx_Senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.Tx_Senha.setReadOnly(False)
        self.Tx_Senha.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.Tx_Senha.setClearButtonEnabled(True)
        self.Tx_Senha.setObjectName("Tx_Senha")
        self.my_progressBar = QtWidgets.QProgressBar(parent=self.widget_Main)
        self.my_progressBar.setGeometry(QtCore.QRect(450, 330, 271, 31))
        self.my_progressBar.setStyleSheet("QProgressBar{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"text-align: center;\n"
"color: rgb(255, 0, 0)\n"
"\n"
"}\n"
"QProgressBar::chunk{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 136, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.my_progressBar.setProperty("value", 0)
        self.my_progressBar.setObjectName("my_progressBar")
        self.Bt_Login = QtWidgets.QPushButton(parent=self.widget_Main)
        self.Bt_Login.setGeometry(QtCore.QRect(450, 260, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_Login.sizePolicy().hasHeightForWidth())
        self.Bt_Login.setSizePolicy(sizePolicy)
        self.Bt_Login.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.Bt_Login.setStyleSheet("QPushButton{\n"
"background:#1E90FF;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:14px;\n"
"}\n"
"QPushButton:hover{\n"
"background:#4169E1;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/login_button.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Bt_Login.setIcon(icon1)
        self.Bt_Login.setIconSize(QtCore.QSize(16, 16))
        self.Bt_Login.setObjectName("Bt_Login")
        self.Bt_Sair = QtWidgets.QPushButton(parent=self.widget_Main)
        self.Bt_Sair.setGeometry(QtCore.QRect(610, 260, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_Sair.sizePolicy().hasHeightForWidth())
        self.Bt_Sair.setSizePolicy(sizePolicy)
        self.Bt_Sair.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.Bt_Sair.setStyleSheet("QPushButton{\n"
"background:#1E90FF;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:14px;\n"
"}\n"
"QPushButton:hover{\n"
"background:#4169E1;\n"
"}")
        self.Bt_Sair.setIcon(icon1)
        self.Bt_Sair.setIconSize(QtCore.QSize(16, 16))
        self.Bt_Sair.setObjectName("Bt_Sair")
        self.Lb_Info_banco = QtWidgets.QLabel(parent=self.widget_Main)
        self.Lb_Info_banco.setGeometry(QtCore.QRect(450, 390, 271, 21))
        self.Lb_Info_banco.setStyleSheet("border: none;\n"
"font: 75 12pt \"Sitka Subheading\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(35, 35, 35);\n"
"\n"
"")
        self.Lb_Info_banco.setText("")
        self.Lb_Info_banco.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Lb_Info_banco.setObjectName("Lb_Info_banco")
        self.Bt_check = QtWidgets.QCheckBox(parent=self.widget_Main)
        self.Bt_check.setGeometry(QtCore.QRect(450, 230, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Bt_check.setFont(font)
        self.Bt_check.setStyleSheet("\n"
"QCheckBox{border:none;}\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(100, 100, 100);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;    \n"
"    \n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 3px solid rgb(255, 205, 0);\n"
"}\n"
"")
        self.Bt_check.setObjectName("Bt_check")
        self.Lb_LcSistemas = QtWidgets.QPushButton(parent=self.widget_Main)
        self.Lb_LcSistemas.setGeometry(QtCore.QRect(450, 30, 271, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lb_LcSistemas.sizePolicy().hasHeightForWidth())
        self.Lb_LcSistemas.setSizePolicy(sizePolicy)
        self.Lb_LcSistemas.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.Lb_LcSistemas.setStyleSheet("QPushButton{\n"
"border: none;\n"
"background-color: rgb(35, 35, 35);\n"
"\n"
"color: rgb(0, 170, 255);\n"
"font: 87 21pt \"Segoe UI Black\";\n"
"}\n"
"QPushButton:hover{\n"
"font: 21pt \"Segoe UI Black\";\n"
"    color: rgb(85, 170, 255);\n"
"\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../img/login-icon-3042.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Lb_LcSistemas.setIcon(icon2)
        self.Lb_LcSistemas.setIconSize(QtCore.QSize(50, 50))
        self.Lb_LcSistemas.setObjectName("Lb_LcSistemas")
        self.Lb_Info = QtWidgets.QLabel(parent=self.widget_Main)
        self.Lb_Info.setGeometry(QtCore.QRect(450, 120, 271, 20))
        self.Lb_Info.setStyleSheet("border: none;\n"
"color: rgb(255, 255, 0);\n"
"font: 75 12pt \"Sitka Subheading\";\n"
"background-color: rgb(35, 35, 35);\n"
"")
        self.Lb_Info.setText("")
        self.Lb_Info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Lb_Info.setObjectName("Lb_Info")
        self.Lb_Direitos = QtWidgets.QLabel(parent=self.widget_Main)
        self.Lb_Direitos.setGeometry(QtCore.QRect(10, 400, 421, 31))
        self.Lb_Direitos.setStyleSheet("border: none;\n"
"background-color: rgb(0, 170, 255);\n"
"font:8pt \"MS Shell Dlg 2\";")
        self.Lb_Direitos.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Lb_Direitos.setObjectName("Lb_Direitos")
        self.Lb_BemVindo = QtWidgets.QLabel(parent=self.widget_Main)
        self.Lb_BemVindo.setGeometry(QtCore.QRect(120, 320, 111, 31))
        self.Lb_BemVindo.setStyleSheet("background-color:none;\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"Arial Rounded MT Bold\";")
        self.Lb_BemVindo.setText("")
        self.Lb_BemVindo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Lb_BemVindo.setObjectName("Lb_BemVindo")
        self.Lb_Nome = QtWidgets.QLabel(parent=self.widget_Main)
        self.Lb_Nome.setGeometry(QtCore.QRect(210, 320, 111, 31))
        self.Lb_Nome.setStyleSheet("background-color:none;\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"Arial Rounded MT Bold\";")
        self.Lb_Nome.setText("")
        self.Lb_Nome.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Lb_Nome.setObjectName("Lb_Nome")
        self.Bt_config_banco = QtWidgets.QPushButton(parent=self.widget_Main)
        self.Bt_config_banco.setGeometry(QtCore.QRect(704, 380, 41, 41))
        self.Bt_config_banco.setStyleSheet("\n"
"background-color: rgb(35, 35, 35);\n"
"border:0px;")
        self.Bt_config_banco.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../img/config.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Bt_config_banco.setIcon(icon3)
        self.Bt_config_banco.setIconSize(QtCore.QSize(35, 35))
        self.Bt_config_banco.setObjectName("Bt_config_banco")
        self.Lb_Info2 = QtWidgets.QLabel(parent=self.widget_Main)
        self.Lb_Info2.setGeometry(QtCore.QRect(450, 300, 271, 21))
        self.Lb_Info2.setStyleSheet("border: none;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt;\n"
"background-color: rgb(35, 35, 35);\n"
"")
        self.Lb_Info2.setText("")
        self.Lb_Info2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Lb_Info2.setObjectName("Lb_Info2")
        self.verticalLayout_2.addWidget(self.widget_Main)
        self.stackedWidget.addWidget(self.Login)
        self.Banco = QtWidgets.QWidget()
        self.Banco.setObjectName("Banco")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Banco)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_5 = QtWidgets.QFrame(parent=self.Banco)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setStyleSheet("background-color: rgb(94, 94, 94);\n"
"border: 0.5px solid black;\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_Main_2 = QtWidgets.QWidget(parent=self.frame_5)
        self.widget_Main_2.setStyleSheet("border:0px solid white;\n"
"background-color: rgb(0, 82, 124);\n"
"\n"
"")
        self.widget_Main_2.setObjectName("widget_Main_2")
        self.frame = QtWidgets.QFrame(parent=self.widget_Main_2)
        self.frame.setGeometry(QtCore.QRect(460, 10, 301, 431))
        self.frame.setStyleSheet("border-top-left-radius: solid 30px;\n"
"background-color: rgb(0, 82, 124);\n"
"color: rgb(255, 255, 255);\n"
"border-bottom-left-radius:solid 12px;\n"
"border:solid 15px ;\n"
"border-radius: 10px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setContentsMargins(5, 0, 0, 0)
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setVerticalSpacing(11)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_14 = QtWidgets.QLabel(parent=self.frame)
        self.label_14.setStyleSheet("font: 8pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 5, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(parent=self.frame)
        self.label_15.setMinimumSize(QtCore.QSize(0, 0))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 1, 1, 1, 1)
        self.LB_Conectado = QtWidgets.QLabel(parent=self.frame)
        self.LB_Conectado.setMaximumSize(QtCore.QSize(16777215, 20))
        self.LB_Conectado.setStyleSheet("color: rgb(0, 255, 127);\n"
"font: 75 10pt \"Microsoft YaHei UI\";")
        self.LB_Conectado.setText("")
        self.LB_Conectado.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LB_Conectado.setObjectName("LB_Conectado")
        self.gridLayout_5.addWidget(self.LB_Conectado, 7, 1, 1, 1)
        self.Lb_LcSistemas_3 = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lb_LcSistemas_3.sizePolicy().hasHeightForWidth())
        self.Lb_LcSistemas_3.setSizePolicy(sizePolicy)
        self.Lb_LcSistemas_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Lb_LcSistemas_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.Lb_LcSistemas_3.setStyleSheet("QPushButton{\n"
"border: none;\n"
"background-color: rgb(0, 82, 124);\n"
"\n"
"color: rgb(0, 170, 255);\n"
"font: 87 17pt \"Segoe UI Black\";\n"
"}\n"
"QPushButton:hover{\n"
"font: 17pt \"Segoe UI Black\";\n"
"    color: rgb(85, 170, 255);\n"
"\n"
"}")
        self.Lb_LcSistemas_3.setIcon(icon1)
        self.Lb_LcSistemas_3.setIconSize(QtCore.QSize(16, 16))
        self.Lb_LcSistemas_3.setObjectName("Lb_LcSistemas_3")
        self.gridLayout_5.addWidget(self.Lb_LcSistemas_3, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.frame)
        self.label_13.setStyleSheet("font: 8pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 4, 0, 1, 1)
        self.Tx_Password = QtWidgets.QLineEdit(parent=self.frame)
        self.Tx_Password.setMinimumSize(QtCore.QSize(0, 25))
        self.Tx_Password.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.Tx_Password.setInputMask("")
        self.Tx_Password.setMaxLength(32765)
        self.Tx_Password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.Tx_Password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Tx_Password.setObjectName("Tx_Password")
        self.gridLayout_5.addWidget(self.Tx_Password, 5, 1, 1, 1)
        self.Tx_Porta = QtWidgets.QLineEdit(parent=self.frame)
        self.Tx_Porta.setMinimumSize(QtCore.QSize(0, 25))
        self.Tx_Porta.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.Tx_Porta.setInputMask("")
        self.Tx_Porta.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Tx_Porta.setObjectName("Tx_Porta")
        self.gridLayout_5.addWidget(self.Tx_Porta, 3, 1, 1, 1)
        self.Tx_Host = QtWidgets.QLineEdit(parent=self.frame)
        self.Tx_Host.setMinimumSize(QtCore.QSize(0, 25))
        self.Tx_Host.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.Tx_Host.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Tx_Host.setObjectName("Tx_Host")
        self.gridLayout_5.addWidget(self.Tx_Host, 2, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(parent=self.frame)
        self.label_16.setStyleSheet("font: 8pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 2, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(parent=self.frame)
        self.label_18.setStyleSheet("font: 8pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 3, 0, 1, 1)
        self.Tx_User = QtWidgets.QLineEdit(parent=self.frame)
        self.Tx_User.setMinimumSize(QtCore.QSize(0, 25))
        self.Tx_User.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.Tx_User.setInputMask("")
        self.Tx_User.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Tx_User.setObjectName("Tx_User")
        self.gridLayout_5.addWidget(self.Tx_User, 4, 1, 1, 1)
        self.LB_Erro = QtWidgets.QLabel(parent=self.frame)
        self.LB_Erro.setMaximumSize(QtCore.QSize(16777215, 20))
        self.LB_Erro.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 10pt \"Microsoft YaHei UI\";\n"
"\n"
"")
        self.LB_Erro.setText("")
        self.LB_Erro.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LB_Erro.setObjectName("LB_Erro")
        self.gridLayout_5.addWidget(self.LB_Erro, 10, 1, 1, 1)
        self.LB_Desconectado = QtWidgets.QLabel(parent=self.frame)
        self.LB_Desconectado.setMaximumSize(QtCore.QSize(16777215, 20))
        self.LB_Desconectado.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 0);")
        self.LB_Desconectado.setText("")
        self.LB_Desconectado.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LB_Desconectado.setObjectName("LB_Desconectado")
        self.gridLayout_5.addWidget(self.LB_Desconectado, 8, 1, 1, 1)
        self.Bt_Desconectar = QtWidgets.QPushButton(parent=self.frame)
        self.Bt_Desconectar.setMinimumSize(QtCore.QSize(0, 25))
        self.Bt_Desconectar.setStyleSheet("QPushButton{\n"
"background:#1E90FF;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:14px;\n"
"}\n"
"QPushButton:hover{\n"
"background:#4169E1;\n"
"}")
        self.Bt_Desconectar.setObjectName("Bt_Desconectar")
        self.gridLayout_5.addWidget(self.Bt_Desconectar, 11, 1, 1, 1)
        self.Bt_Conectar = QtWidgets.QPushButton(parent=self.frame)
        self.Bt_Conectar.setMinimumSize(QtCore.QSize(0, 25))
        self.Bt_Conectar.setStyleSheet("QPushButton{\n"
"background:#1E90FF;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:14px;\n"
"}\n"
"QPushButton:hover{\n"
"background:#4169E1;\n"
"}\n"
"")
        self.Bt_Conectar.setObjectName("Bt_Conectar")
        self.gridLayout_5.addWidget(self.Bt_Conectar, 11, 0, 1, 1)
        self.Bt_Tela_Login = QtWidgets.QPushButton(parent=self.widget_Main_2)
        self.Bt_Tela_Login.setGeometry(QtCore.QRect(10, 370, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_Tela_Login.sizePolicy().hasHeightForWidth())
        self.Bt_Tela_Login.setSizePolicy(sizePolicy)
        self.Bt_Tela_Login.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.Bt_Tela_Login.setStyleSheet("QPushButton{\n"
"background:#1E90FF;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:14px;\n"
"}\n"
"QPushButton:hover{\n"
"background:#4169E1;\n"
"}")
        self.Bt_Tela_Login.setIcon(icon1)
        self.Bt_Tela_Login.setIconSize(QtCore.QSize(16, 16))
        self.Bt_Tela_Login.setObjectName("Bt_Tela_Login")
        self.Bt_Sair_4 = QtWidgets.QPushButton(parent=self.widget_Main_2)
        self.Bt_Sair_4.setGeometry(QtCore.QRect(270, 370, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_Sair_4.sizePolicy().hasHeightForWidth())
        self.Bt_Sair_4.setSizePolicy(sizePolicy)
        self.Bt_Sair_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.Bt_Sair_4.setStyleSheet("QPushButton{\n"
"background:#1E90FF;\n"
"color:white;\n"
"font-family: Trebuchet MS;\n"
"font-weight:bold;\n"
"font-size:14px;\n"
"}\n"
"QPushButton:hover{\n"
"background:#4169E1;\n"
"}")
        self.Bt_Sair_4.setIcon(icon1)
        self.Bt_Sair_4.setIconSize(QtCore.QSize(16, 16))
        self.Bt_Sair_4.setObjectName("Bt_Sair_4")
        self.Lb_Direitos_2 = QtWidgets.QLabel(parent=self.widget_Main_2)
        self.Lb_Direitos_2.setGeometry(QtCore.QRect(10, 410, 371, 31))
        self.Lb_Direitos_2.setStyleSheet("border: none;\n"
"background-color: rgb(0, 170, 255);\n"
"font:8pt \"MS Shell Dlg 2\";\n"
"border-bottom-right-radius:30px;\n"
"border-top-left-radius:30px;")
        self.Lb_Direitos_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Lb_Direitos_2.setObjectName("Lb_Direitos_2")
        self.Lb_Background_2 = QtWidgets.QLabel(parent=self.widget_Main_2)
        self.Lb_Background_2.setGeometry(QtCore.QRect(10, 10, 371, 321))
        self.Lb_Background_2.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0.518552, y1:0.414227, x2:0.52957, y2:1, stop:0 #00aaff, stop:1 rgb(47, 163, 163));\n"
"\n"
"border-top-left-radius:30px;\n"
"border-bottom-right-radius:30px;\n"
"\n"
"\n"
"\n"
"border:0px;\n"
"\n"
"\n"
"background-repeat: no-repeat;\n"
"\n"
" background-repeat: no-repeat;\n"
"background-position: center;\n"
"\n"
"")
        self.Lb_Background_2.setText("")
        self.Lb_Background_2.setPixmap(QtGui.QPixmap("../../WERWER.png"))
        self.Lb_Background_2.setScaledContents(True)
        self.Lb_Background_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Lb_Background_2.setObjectName("Lb_Background_2")
        self.verticalLayout_3.addWidget(self.widget_Main_2)
        self.gridLayout_2.addWidget(self.frame_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.Banco)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        Form_Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Form_Login)
        self.stackedWidget.setCurrentIndex(0)
        self.Bt_Sair_4.pressed.connect(Form_Login.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form_Login)
        Form_Login.setTabOrder(self.Tx_Usuario, self.Tx_Senha)
        Form_Login.setTabOrder(self.Tx_Senha, self.Bt_check)
        Form_Login.setTabOrder(self.Bt_check, self.Bt_Login)
        Form_Login.setTabOrder(self.Bt_Login, self.Bt_Sair)
        Form_Login.setTabOrder(self.Bt_Sair, self.Bt_config_banco)
        Form_Login.setTabOrder(self.Bt_config_banco, self.Tx_Host)
        Form_Login.setTabOrder(self.Tx_Host, self.Tx_Porta)
        Form_Login.setTabOrder(self.Tx_Porta, self.Tx_User)
        Form_Login.setTabOrder(self.Tx_User, self.Tx_Password)
        Form_Login.setTabOrder(self.Tx_Password, self.Bt_Conectar)
        Form_Login.setTabOrder(self.Bt_Conectar, self.Bt_Desconectar)
        Form_Login.setTabOrder(self.Bt_Desconectar, self.Bt_Tela_Login)
        Form_Login.setTabOrder(self.Bt_Tela_Login, self.Bt_Sair_4)
        Form_Login.setTabOrder(self.Bt_Sair_4, self.Lb_LcSistemas_3)
        Form_Login.setTabOrder(self.Lb_LcSistemas_3, self.Lb_LcSistemas)

    def retranslateUi(self, Form_Login):
        _translate = QtCore.QCoreApplication.translate
        Form_Login.setWindowTitle(_translate("Form_Login", "LC INFORMÁTICA | LOGIN"))
        self.Tx_Usuario.setPlaceholderText(_translate("Form_Login", "Usuario"))
        self.Tx_Senha.setPlaceholderText(_translate("Form_Login", "Senha"))
        self.Bt_Login.setText(_translate("Form_Login", " Confirmar"))
        self.Bt_Sair.setText(_translate("Form_Login", "sair"))
        self.Bt_check.setToolTip(_translate("Form_Login", "Clique aqui para visualizar e ocultar a senha"))
        self.Bt_check.setText(_translate("Form_Login", "Visualizar"))
        self.Lb_LcSistemas.setText(_translate("Form_Login", "Login"))
        self.Lb_Direitos.setText(_translate("Form_Login", "Todos os direitos reservados © LC INFORMÁTICA"))
        self.Bt_config_banco.setToolTip(_translate("Form_Login", "Configuração do banco de dados"))
        self.label_14.setText(_translate("Form_Login", "SENHA:"))
        self.label_15.setText(_translate("Form_Login", "Configuração do banco de dados"))
        self.Lb_LcSistemas_3.setText(_translate("Form_Login", "LC INFORMÁTICA"))
        self.label_13.setText(_translate("Form_Login", "USUÁRIO:"))
        self.Tx_Password.setPlaceholderText(_translate("Form_Login", "Minimo 4 dígtos"))
        self.Tx_Porta.setPlaceholderText(_translate("Form_Login", "Porta"))
        self.Tx_Host.setInputMask(_translate("Form_Login", "000.000.00.000"))
        self.Tx_Host.setPlaceholderText(_translate("Form_Login", "0.0.0.0"))
        self.label_16.setText(_translate("Form_Login", "IP SERVIDOR:"))
        self.label_18.setText(_translate("Form_Login", "PORTA:"))
        self.Tx_User.setPlaceholderText(_translate("Form_Login", "Usuário"))
        self.Bt_Desconectar.setText(_translate("Form_Login", "Desconectar"))
        self.Bt_Conectar.setText(_translate("Form_Login", "Conectar"))
        self.Bt_Tela_Login.setText(_translate("Form_Login", "Tela de Login"))
        self.Bt_Sair_4.setText(_translate("Form_Login", "Sair"))
        self.Lb_Direitos_2.setText(_translate("Form_Login", "Todos os direitos reservados © LC INFORMÁTICA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Login = QtWidgets.QMainWindow()
    ui = Ui_Form_Login()
    ui.setupUi(Form_Login)
    Form_Login.show()
    sys.exit(app.exec())
