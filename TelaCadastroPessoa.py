from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
from conexao import conectar
from TelaHome import TelaHome

class TelaCadastroPessoa(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Pessoa")
        self.setGeometry(200, 200, 400, 300)

        layout_principal = QVBoxLayout()

        # Barra de navegação
        navbar_layout = QHBoxLayout()

        # Botões da barra de navegação
        botao_home = QPushButton("Home",clicked=self.voltar_home)
        botao_estoque = QPushButton("Estoque")
        botao_pedido = QPushButton("Pedido")
        botao_fornecedor = QPushButton("Fornecedor")
        botao_relatorio = QPushButton("Relatório")
        botao_caixa = QPushButton("Caixa")
        botao_calendario = QPushButton("Calendário")
        botao_calculadora = QPushButton("Calculadora")

        # Adiciona os botões à barra de navegação
        navbar_layout.addWidget(botao_home)
        navbar_layout.addWidget(botao_estoque)
        navbar_layout.addWidget(botao_pedido)
        navbar_layout.addWidget(botao_fornecedor)
        navbar_layout.addWidget(botao_relatorio)
        navbar_layout.addWidget(botao_caixa)
        navbar_layout.addWidget(botao_calendario)
        navbar_layout.addWidget(botao_calculadora)

        # Widget para conter a barra de navegação
        navbar_widget = QWidget()
        navbar_widget.setLayout(navbar_layout)

        # Adiciona a barra de navegação ao layout principal
        layout_principal.addWidget(navbar_widget)

        # Adiciona os campos de entrada ao layout principal
        layout_principal.addWidget(QLabel("Nome:"))
        self.entry_nome = QLineEdit()
        layout_principal.addWidget(self.entry_nome)

        layout_principal.addWidget(QLabel("CPF/CNPJ:"))
        self.entry_cpf_cnpj = QLineEdit()
        layout_principal.addWidget(self.entry_cpf_cnpj)

        layout_principal.addWidget(QLabel("Endereço:"))
        self.entry_endereco = QLineEdit()
        layout_principal.addWidget(self.entry_endereco)

        layout_principal.addWidget(QLabel("Telefone:"))
        self.entry_telefone = QLineEdit()
        layout_principal.addWidget(self.entry_telefone)

        # Adiciona espaçamento entre os campos de entrada e os botões
        layout_principal.addSpacing(20)

        # Adiciona os botões ao layout principal
        layout_principal.addWidget(QPushButton("Salvar", clicked=self.salvar_pessoa))
        layout_principal.addWidget(QPushButton("Voltar para Home", clicked=self.voltar_home))

        central_widget = QWidget()
        central_widget.setLayout(layout_principal)
        self.setCentralWidget(central_widget)

    def salvar_pessoa(self):
        nome = self.entry_nome.text()
        cpf_cnpj = self.entry_cpf_cnpj.text()
        endereco = self.entry_endereco.text()
        telefone = self.entry_telefone.text()

        # Conecta ao banco de dados
        conexao = conectar()

        # Executa a consulta SQL para inserir os dados
        cursor = conexao.cursor()
        consulta = ("INSERT INTO clientes (nome, cpf_cnpj, endereco, telefone) VALUES (%s, %s, %s, %s)")
        dados = (nome, cpf_cnpj, endereco, telefone)
        cursor.execute(consulta, dados)

        # Confirma a transação e fecha a conexão
        conexao.commit()
        cursor.close()
        conexao.close()

        print("Dados inseridos no banco de dados com sucesso!")

    def voltar_home(self):
        self.hide()
        self.tela_home = TelaHome()
        self.tela_home.show()
