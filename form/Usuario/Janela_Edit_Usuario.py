from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from form.Usuario.Form_Edit_Usuario import Ui_Form_Edit_Usuario

class Classe_Edit_Usuario(QMainWindow, Ui_Form_Edit_Usuario):
    def __init__(self):
        super(Classe_Edit_Usuario, self).__init__()
        self.setupUi(self)
    

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    system = Classe_Edit_Usuario()
    system.show()
    sys.exit(app.exec())