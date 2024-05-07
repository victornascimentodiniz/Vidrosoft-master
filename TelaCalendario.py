from PyQt5.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtWidgets import QCalendarWidget, QTextEdit, QMessageBox, QInputDialog
from PyQt5.QtGui import QTextCharFormat, QColor
from PyQt5.QtCore import Qt, pyqtSignal

class TelaCalendario(QMainWindow):
    voltar_para_home_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendário")
        self.setGeometry(300, 300, 800, 400)

        # Barra de navegação
        self.navbar_layout = QHBoxLayout()

        # Botões da barra de navegação
        botao_home = QPushButton("Home")
        botao_cadastro_pessoa = QPushButton("Cadastro de Pessoa")
        botao_calculadora = QPushButton("Calculadora")
        botao_estoque = QPushButton("Estoque")
        botao_pedido = QPushButton("Pedido")
        botao_fornecedor = QPushButton("Fornecedor")
        botao_relatorio = QPushButton("Relatório")
        botao_caixa = QPushButton("Caixa")

        # Adiciona os botões à barra de navegação
        self.navbar_layout.addWidget(botao_home)
        self.navbar_layout.addWidget(botao_cadastro_pessoa)
        self.navbar_layout.addWidget(botao_calculadora)
        self.navbar_layout.addWidget(botao_estoque)
        self.navbar_layout.addWidget(botao_pedido)
        self.navbar_layout.addWidget(botao_fornecedor)
        self.navbar_layout.addWidget(botao_relatorio)
        self.navbar_layout.addWidget(botao_caixa)

        # Widget para conter a barra de navegação
        navbar_widget = QWidget()
        navbar_widget.setLayout(self.navbar_layout)

        # Adiciona a barra de navegação à janela principal
        self.setMenuWidget(navbar_widget)

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
