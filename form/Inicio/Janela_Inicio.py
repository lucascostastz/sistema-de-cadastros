from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from form.Inicio.Form_Inicio import Ui_Form_Inicio


class Classe_Inicio(QMainWindow, Ui_Form_Inicio):
    def __init__(self):
        super(Classe_Inicio, self).__init__()
        self.setupUi(self)
    

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Inicio()
    system.show()
    sys.exit(app.exec())