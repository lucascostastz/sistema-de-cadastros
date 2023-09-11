import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Botão Bloqueado/Oculto")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        layout = QVBoxLayout()
        
        self.button = QPushButton("Clique em mim!")
        self.button.clicked.connect(self.toggle_button)
        
        layout.addWidget(self.button)
        self.central_widget.setLayout(layout)

    def toggle_button(self):
        if self.button.isEnabled():
            self.button.setEnabled(False)  # Bloqueia o botão
            # self.button.hide()  # Para ocultar o botão

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
