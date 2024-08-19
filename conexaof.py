import sqlite3

conexao = sqlite3.connect("bancoF")
cursor = conexao.cursor()

# cursor.execute(
#     "CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));"
# )

# cursor.execute(
#     "INSERT INTO produtos(id, nome, endereco, email) VALUES (1, 'Dani', 'bromelia', 'dani@gmail.com');"
# )
# cursor.execute(
#     "INSERT INTO produtos(id, nome, endereco, email) VALUES (2, 'Frank', 'Por Ali', 'Frank@gmail.com');"
# )
# cursor.execute(
#     "INSERT INTO produtos(id, nome, endereco, email) VALUES (3, 'Valdemar', 'Ali Perto', 'Val@gmail.com');"
# )
# cursor.execute(
#     "INSERT INTO produtos(id, nome, endereco, email) VALUES (4, 'Fabio', 'flor', 'Fabio@gmail.com');"
# )
# cursor.execute(
#     "INSERT INTO produtos(id, nome, endereco, email) VALUES (5, 'Maria', 'rosas', 'Maria@gmail.com');"
# )
# cursor.execute("DELETE FROM usuario where id=1") deleta dados inseridos na tabela
# dado = cursor.execute("SELECT * FROM produtos")
# ORDER BY DESC
dado = cursor.execute(
    "SELECT * FROM produtos ORDER BY nome "
)  # ordena na ordem alfabetica
# dado = cursor.execute("SELECT * FROM produtos ORDER BY nome DESC")   ordena descresente

# LIMIT E DISTINCT
# dado = cursor.execute("SELECT * FROM produtos LIMIT 3")
for produtos in dado:
    print(produtos)
# cursor.execute('UPDATE usuario SET endereco="Minha Rua" WHERE nome="Valdemar"')
conexao.commit()
conexao.close
# para ocorre tudo certo conexão com banco de dado sqlite tem entra na pasta roda a python conexaoC.py
