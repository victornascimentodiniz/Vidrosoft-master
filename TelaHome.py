from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QComboBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from TelaCalendario import TelaCalendario
from TelaCalculadora import TelaCalculadora

class TelaHome(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home")
        self.setGeometry(100, 100, 800, 600)

        label_bem_vindo = QLabel("Bem-vindo à tela Home!", self)
        label_bem_vindo.setGeometry(50, 50, 300, 50)

        botoes_esquerda = [("Cadastro de Pessoa", "icons8-cadastro-50.png", self.abrir_tela_cadastro_pessoa),
                           ("Estoque", "caixa.png", None),
                           ("Pedido", "lista-de-controle.png", None),
                           ("Fornecedores", "icons8-fornecedor-50.png", None)]

        botoes_direita = [("Calendário", "icone_calendario.png", self.abrir_tela_calendario),
                          ("Calculadora", "icone_orcamento.png", self.abrir_tela_calculadora),
                          ("Relatórios", "icone_relatorio.png", None),
                          ("Caixa", "icone_caixa.png", None)]

        layout_principal = QHBoxLayout(self)
        layout_esquerda = QVBoxLayout()
        layout_direita = QVBoxLayout()

        for texto, icone, comando in botoes_esquerda:
            botao = QPushButton(texto, self)
            botao.setIcon(QIcon(QPixmap(icone).scaled(30, 30)))
            botao.setIconSize(QPixmap(icone).size())
            botao.setFixedSize(150, 60)
            if comando:
                botao.clicked.connect(comando)
            layout_esquerda.addWidget(botao)

        for texto, icone, comando in botoes_direita:
            botao = QPushButton(texto, self)
            botao.setIcon(QIcon(QPixmap(icone).scaled(30, 30)))
            botao.setIconSize(QPixmap(icone).size())
            botao.setFixedSize(150, 60)
            if comando:
                botao.clicked.connect(comando)
            layout_direita.addWidget(botao)

        layout_principal.addLayout(layout_esquerda)
        layout_principal.addLayout(layout_direita)

        central_widget = QWidget(self)
        central_widget.setLayout(layout_principal)
        self.setCentralWidget(central_widget)

    def abrir_tela_cadastro_pessoa(self):
        self.hide()  # Esconde a tela home
        from TelaCadastroPessoa import TelaCadastroPessoa
        self.tela_cadastro_pessoa = TelaCadastroPessoa()  # Abre a tela de cadastro de pessoa
        self.tela_cadastro_pessoa.show()  # Exibe a tela de cadastro de pessoa

    def abrir_tela_calendario(self):
        self.hide()  # Esconde a tela home
        self.tela_calendario = TelaCalendario()  # Abre a tela de calendário
        self.tela_calendario.show()  # Exibe a tela de calendário

    def abrir_tela_calculadora(self):
        self.hide()  # Esconde a tela home
        self.tela_calculadora = TelaCalculadora()  # Abre a tela da calculadora
        self.tela_calculadora.show()  # Exibe a tela da calculadora
