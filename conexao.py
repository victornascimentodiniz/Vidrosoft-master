# No arquivo conexao.py
import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="vidrasoft"
    )
    if conexao.is_connected():
        print("Conexão bem sucedida!")
    return conexao
