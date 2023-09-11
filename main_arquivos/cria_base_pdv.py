import mysql.connector
import sqlite3


def criar_tabelas():
  bc = sqlite3.connect('banco.db')
  cur = bc.cursor() 
  cur.execute("SELECT *FROM informacoes")
  dados_lidos = cur.fetchall()
  ip = dados_lidos[0][0]
  porta = dados_lidos[0][1]
  usuario = dados_lidos[0][2]
  senha = dados_lidos[0][3]
  banco = mysql.connector.connect(
  host=ip,
  user=usuario,
  port=porta,
  password=senha)
  # Crie um objeto cursor
  mycursor = banco.cursor()
  # Crie um banco de dados
  mycursor.execute("CREATE DATABASE if not exists pdv")
  # Use o banco de dados
  mycursor.execute("USE pdv")
  # Crie uma tabela
  mycursor.execute("CREATE TABLE if not exists usuarios (idusuarios INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(45), login VARCHAR(45), senha1 VARCHAR(45), senha2 VARCHAR(45), nivel_de_acesso VARCHAR(45), permissao VARCHAR(45))")
  mycursor.execute("INSERT INTO usuarios (nome, login, senha1, senha2, nivel_de_acesso, permissao) VALUES ('ADMIN', 'ADMIN', 'ADMIN', 'ADMIN', 'ADMINISTRADOR', 'TODAS')")
  mycursor.execute("CREATE TABLE if not exists produtos(idprodutos INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, descricao VARCHAR(45), categoria VARCHAR(45), marca VARCHAR(45), estoque VARCHAR(45), codigo VARCHAR(45), preco VARCHAR(45), v_varejo VARCHAR(45), v_atacado VARCHAR(45), qm_atacado VARCHAR(45), imagem VARCHAR(150))")
  mycursor.execute("CREATE TABLE if not exists clientes (idclientes INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY , nome VARCHAR(50), cpf VARCHAR(45), rg VARCHAR(45), telefone VARCHAR(45), email VARCHAR(45), cep VARCHAR(45), endereco VARCHAR(45), numero VARCHAR(45), bairro VARCHAR(45), cidade VARCHAR(45), estado VARCHAR(45))")
  banco.commit()
  # Feche o cursor e a conexão com o banco de dados
  mycursor.close()
  banco.close()
criar_tabelas()

