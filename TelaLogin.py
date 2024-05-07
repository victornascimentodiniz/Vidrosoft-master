import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from TelaHome import TelaHome  # Importe aqui dentro do método necessário

class TelaLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 400, 300)

        label_email_login = QLabel("Email:", self)
        label_email_login.setGeometry(20, 50, 60, 20)

        self.entry_email_login = QLineEdit(self)
        self.entry_email_login.setGeometry(100, 50, 200, 20)

        label_senha_login = QLabel("Senha:", self)
        label_senha_login.setGeometry(20, 100, 60, 20)

        self.entry_senha_login = QLineEdit(self)
        self.entry_senha_login.setGeometry(100, 100, 200, 20)
        self.entry_senha_login.setEchoMode(QLineEdit.Password)

        botao_login = QPushButton("Login", self)
        botao_login.setGeometry(150, 150, 100, 30)
        botao_login.clicked.connect(self.fazer_login)

    def fazer_login(self):
        email_digitado = self.entry_email_login.text()
        senha_digitada = self.entry_senha_login.text()

        print("Email digitado:", email_digitado)
        print("Senha digitada:", senha_digitada)

        if email_digitado == "123" and senha_digitada == "123":
            self.hide()
            from TelaHome import TelaHome  # Importe aqui dentro do método necessário
            self.tela_home = TelaHome()
            self.tela_home.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_login = TelaLogin()
    tela_login.show()
    sys.exit(app.exec_())
