from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget, QApplication
from PyQt5.QtCore import Qt

class TelaCalculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setGeometry(400, 200, 300, 400)

        # Barra de navegação
        navbar_layout = QHBoxLayout()
        botao_home = QPushButton("Home", clicked=self.voltar_home)
        botao_cadastro_pessoa = QPushButton("Cadastro de Pessoa")
        botao_calendario = QPushButton("Calendário")
        botao_estoque = QPushButton("Estoque")  # Novo botão
        botao_pedido = QPushButton("Pedido")  # Novo botão
        botao_fornecedor = QPushButton("Fornecedor")  # Novo botão
        botao_relatorio = QPushButton("Relatório")  # Novo botão
        botao_caixa = QPushButton("Caixa")  # Novo botão
        
        navbar_layout.addWidget(botao_home)
        navbar_layout.addWidget(botao_cadastro_pessoa)
        navbar_layout.addWidget(botao_calendario)
        navbar_layout.addWidget(botao_estoque)  # Adicionando o botão "Estoque"
        navbar_layout.addWidget(botao_pedido)  # Adicionando o botão "Pedido"
        navbar_layout.addWidget(botao_fornecedor)  # Adicionando o botão "Fornecedor"
        navbar_layout.addWidget(botao_relatorio)  # Adicionando o botão "Relatório"
        navbar_layout.addWidget(botao_caixa)  # Adicionando o botão "Caixa"
        
        navbar_widget = QWidget()
        navbar_widget.setLayout(navbar_layout)
        navbar_widget.setFixedHeight(50)  # Definindo a altura fixa da barra de navegação

        # Display da calculadora
        self.display = QLineEdit(self)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        # Layout da calculadora
        layout_calculadora = QGridLayout()
        buttons = [
            ("7", (0, 0)),
            ("8", (0, 1)),
            ("9", (0, 2)),
            ("4", (1, 0)),
            ("5", (1, 1)),
            ("6", (1, 2)),
            ("1", (2, 0)),
            ("2", (2, 1)),
            ("3", (2, 2)),
            ("0", (3, 0)),
            ("C", (3, 1)),
            ("CE", (3, 2)),
            ("+", (0, 3)),
            ("-", (1, 3)),
            ("*", (2, 3)),
            ("/", (3, 3)),
            ("=", (3, 4)),
        ]
        for (text, pos) in buttons:
            button = QPushButton(text)
            if text in {"C", "CE", "="}:
                button.clicked.connect(self.on_click)
            else:
                button.clicked.connect(self.append_text)
            layout_calculadora.addWidget(button, *pos)

        # Layout principal
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(navbar_widget)
        layout_principal.addWidget(self.display)
        layout_principal.addStretch()
        layout_principal.addLayout(layout_calculadora)

        central_widget = QWidget(self)
        central_widget.setLayout(layout_principal)
        self.setCentralWidget(central_widget)

        # Alinhando o layout principal ao topo da janela
        self.layout().setAlignment(Qt.AlignTop)

    def on_click(self):
        button = self.sender()
        if button is None:
            print("Botão é None!")
            return

        text = button.text()

        if text == "=":
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception as e:
                self.display.setText("Error")
        elif text == "C":
            self.display.backspace()  
        elif text == "CE":
            self.display.clear()

    def append_text(self):
        button = self.sender()
        text = button.text()
        self.display.setText(self.display.text() + text)
    def voltar_home(self):
        self.hide()
        self.tela_home = TelaHome()
        self.tela_home.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    tela = TelaCalculadora()
    tela.show()
    sys.exit(app.exec_())
