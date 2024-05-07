import sys
from PyQt5.QtWidgets import QApplication
from TelaLogin import TelaLogin
from TelaHome import TelaHome
from TelaCalendario import TelaCalendario

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    tela_login = TelaLogin()
    tela_home = TelaHome()
    tela_calendario = TelaCalendario()

    tela_login.show()

    # Conectando o sinal voltar_para_home_signal da tela de calendário ao método show da tela home
    tela_calendario.voltar_para_home_signal.connect(tela_home.show)

    sys.exit(app.exec_())
