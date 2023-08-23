import sqlite3 as sql

#Iniciando a conexão com o banco de dados.
conexao = sql.connect('bancodedados.db')

#Apontador do banco de dados.
cursor = conexao.cursor()

#Colocar informações no banco de dados
cursor.execute("INSERT INTO tabela VALUES (null, 'Mirian', 16)")
#cursor.execute("INSERT INTO tabela (nome,idade) VALUES(?,?)", ('José',44))
#cursor.execute("INSERT INTO TABELA (nome, idade) VALUES ('Igor', '49')")

#Comitar/enviar as informações ao banco de dados
conexao.commit()


#Encerrando a conexão com bando de dados.
conexao.close()