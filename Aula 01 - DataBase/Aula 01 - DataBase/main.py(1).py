import sqlite3 as sql

#Iniciando a conexão com o banco de dados:
conexao = sql.connect('bancodedados.db')

#Apontador do banco de dados:
cursor = conexao.cursor()

#Ler informações do banco de dados: - Cria uma lista, com várias tuplas contendo as informações
dado = cursor.execute("SELECT nome, idade FROM tabela WHERE id =?", (2,)).fetchall()
dado_tudo = cursor.execute("SELECT nome, idade FROM tabela WHERE id =?", (2,)).fetchall()

'''for dados in dado:
    print(f"Nome:{dados[0]}")
    print(f"Idade:{dados[1]}\n")'''

#Comitar/enviar as informações ao banco de dados:
conexao.commit()


#Encerrando a conexão com bando de dados:
conexao.close()