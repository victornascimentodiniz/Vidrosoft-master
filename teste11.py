import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget, QDateEdit, QComboBox, QCalendarWidget, QMessageBox, QTextEdit, QInputDialog, QGridLayout
from PyQt5.QtGui import QIcon, QPixmap, QTextCharFormat, QColor
from PyQt5.QtCore import Qt

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
            self.tela_home = TelaHome()
            self.tela_home.show()

class TelaHome(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home")
        self.setGeometry(100, 100, 800, 600)

        label_bem_vindo = QLabel("Bem-vindo à tela Home!", self)
        label_bem_vindo.setGeometry(50, 50, 300, 50)

        botoes_esquerda = [("Cadastro de Pessoa", "D:\\DOCUMENTOS\\Downloads\\icons8-cadastro-50.png", self.abrir_tela_cadastro_pessoa),
                           ("Estoque", "D:\\DOCUMENTOS\\Downloads\\caixa.png", None),
                           ("Pedido", "D:\\DOCUMENTOS\\Downloads\\lista-de-controle.png", None),
                           ("Fornecedores", "D:\\DOCUMENTOS\\Downloads\\icons8-fornecedor-50.png", None)]

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

class TelaCalendario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendário")
        self.setGeometry(300, 300, 800, 400)

        self.calendario = QCalendarWidget(self)
        self.calendario.setGeometry(50, 50, 300, 300)
        self.calendario.clicked.connect(self.mostrar_tarefas)

        self.tarefas = {}

        self.text_edit_tarefa = QTextEdit(self)
        self.text_edit_tarefa.setGeometry(400, 50, 300, 200)
        self.text_edit_tarefa.setReadOnly(True)

        self.botao_adicionar_tarefa = QPushButton("Adicionar Tarefa", self)
        self.botao_adicionar_tarefa.setGeometry(400, 270, 200, 30)
        self.botao_adicionar_tarefa.clicked.connect(self.adicionar_tarefa)

        self.botao_voltar_home = QPushButton("Voltar para Home", self)
        self.botao_voltar_home.setGeometry(400, 310, 200, 30)
        self.botao_voltar_home.clicked.connect(self.voltar_home)

    def mostrar_tarefas(self, date):
        data_str = date.toString("dd/MM/yyyy")
        tarefas = self.tarefas.get(data_str)
        if tarefas:
            self.text_edit_tarefa.setPlainText("\n".join(tarefas))
        else:
            self.text_edit_tarefa.setPlainText("Não há tarefas para este dia.")

    def adicionar_tarefa(self):
        date = self.calendario.selectedDate()
        data_str = date.toString("dd/MM/yyyy")
        tarefa, ok = QInputDialog.getText(self, "Adicionar Tarefa", "Digite a tarefa:")
        if ok and tarefa.strip():
            if data_str in self.tarefas:
                self.tarefas[data_str].append(tarefa)
            else:
                self.tarefas[data_str] = [tarefa]

            self.atualizar_cor_data(date)

            QMessageBox.information(self, "Tarefa Adicionada", f"Tarefa adicionada em {data_str}.")

    def atualizar_cor_data(self, date):
        format = QTextCharFormat()
        cor = QColor(255, 165, 0)  # Cor laranja
        format.setForeground(cor)
        self.calendario.setDateTextFormat(date, format)

    def voltar_home(self):
        self.hide()
        self.tela_home = TelaHome()
        self.tela_home.show()

class TelaCalculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setGeometry(400, 200, 300, 400)

        self.display = QLineEdit(self)
        self.display.setGeometry(10, 10, 280, 50)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        layout = QGridLayout()

        buttons = [
            ("/", (0, 3)),
            ("*", (1, 3)),
            ("-", (2, 3)),
            ("+", (3, 3)),
            ("=", (3, 2))
        ]

        for (text, pos) in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.on_click)
            layout.addWidget(button, *pos)

        for i in range(10):
            button = QPushButton(str(i))
            button.clicked.connect(self.on_click)
            row = i // 3
            col = i % 3
            layout.addWidget(button, row, col)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_click(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception as e:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)

class TelaCadastroPessoa(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Pessoa")
        self.setGeometry(200, 200, 400, 400)

        label_nome = QLabel("Nome completo:", self)
        label_nome.setGeometry(20, 20, 100, 20)

        self.entry_nome = QLineEdit(self)
        self.entry_nome.setGeometry(150, 20, 200, 20)

        label_nascimento = QLabel("Data de nascimento:", self)
        label_nascimento.setGeometry(20, 50, 120, 20)

        self.entry_nascimento = QDateEdit(self)
        self.entry_nascimento.setGeometry(150, 50, 120, 20)
        self.entry_nascimento.setCalendarPopup(True)

        label_genero = QLabel("Gênero:", self)
        label_genero.setGeometry(20, 80, 60, 20)

        self.combo_genero = QComboBox(self)
        self.combo_genero.setGeometry(150, 80, 120, 20)
        self.combo_genero.addItems(["Masculino", "Feminino", "Outro"])

        label_nacionalidade = QLabel("Nacionalidade:", self)
        label_nacionalidade.setGeometry(20, 110, 100, 20)

        self.entry_nacionalidade = QLineEdit(self)
        self.entry_nacionalidade.setGeometry(150, 110, 200, 20)

        label_endereco = QLabel("Endereço residencial:", self)
        label_endereco.setGeometry(20, 140, 120, 20)

        self.entry_endereco = QLineEdit(self)
        self.entry_endereco.setGeometry(150, 140, 200, 20)

        label_telefone = QLabel("Número de telefone:", self)
        label_telefone.setGeometry(20, 170, 120, 20)

        self.entry_telefone = QLineEdit(self)
        self.entry_telefone.setGeometry(150, 170, 120, 20)

        label_email = QLabel("Endereço de e-mail:", self)
        label_email.setGeometry(20, 200, 120, 20)

        self.entry_email = QLineEdit(self)
        self.entry_email.setGeometry(150, 200, 200, 20)

        label_identificacao = QLabel("Número de identificação pessoal:", self)
        label_identificacao.setGeometry(20, 230, 200, 20)

        self.entry_identificacao = QLineEdit(self)
        self.entry_identificacao.setGeometry(220, 230, 130, 20)

        botao_salvar = QPushButton("Salvar", self)
        botao_salvar.setGeometry(150, 290, 100, 30)
        botao_salvar.clicked.connect(self.salvar_pessoa)

        self.botao_voltar_home = QPushButton("Voltar para Home", self)
        self.botao_voltar_home.setGeometry(150, 330, 200, 30)
        self.botao_voltar_home.clicked.connect(self.voltar_home)

    def salvar_pessoa(self):
        nome = self.entry_nome.text()
        nascimento = self.entry_nascimento.date().toString("dd/MM/yyyy")
        genero = self.combo_genero.currentText()
        nacionalidade = self.entry_nacionalidade.text()
        endereco = self.entry_endereco.text()
        telefone = self.entry_telefone.text()
        email = self.entry_email.text()
        identificacao = self.entry_identificacao.text()

        print("Nome:", nome)
        print("Data de nascimento:", nascimento)
        print("Gênero:", genero)
        print("Nacionalidade:", nacionalidade)
        print("Endereço residencial:", endereco)
        print("Número de telefone:", telefone)
        print("Endereço de e-mail:", email)
        print("Número de identificação pessoal:", identificacao)

    def voltar_home(self):
        self.hide()
        self.tela_home = TelaHome()
        self.tela_home.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_login = TelaLogin()
    tela_login.show()
    sys.exit(app.exec_())
