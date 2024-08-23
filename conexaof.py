import sqlite3

conexao = sqlite3.connect("bancoF")
cursor = conexao.cursor()

# Criando Tabela Autores
# cursor.execute(
#     """
#     CREATE TABLE Autores(
#     autor_id INT,
#     nome VARCHAR(100),
#     nacionalidade VARCHAR(50));
#     """
# )

# Inserindo Autores
# cursor.execute(
#     """
#     INSERT INTO Autores (autor_id, nome, nacionalidade)
#     VALUES
#     (1, 'Caíque Cardoso', 'Brasileiro'),
#     (2, 'Simon Collison', 'Americano'),
#     (3, 'Machado de Assis', 'Brasileiro'),
#     (4, 'Clarice Líspecto', 'Brasileiro');
#     """
# )

# Criando Tabela Editoras
# cursor.execute(
#     """
#     CREATE TABLE Editoras(
#     editora_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome VARCHAR(100) NOT NULL);
#     """
# )

# Inserindo Editoras
# cursor.execute(
#     """
#     INSERT INTO Editoras (editora_id, nome)
#     VALUES
#     (1, 'Editora Ciência Moderna'),
#     (2, 'Alta Books'),
#     (3, 'Editora Saraiva'),
#     (4, 'Penguin Books');
#     """
# )

# Criando Tabela de Livro
# cursor.execute(
#     """
#     CREATE TABLE Livros (
#     livro_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     titulo TEXT NOT NULL,
#     editora_id INTEGER,
#     max_renovacoes INTEGER,
#     FOREIGN KEY (editora_id) REFERENCES Editoras(editora_id));
#     """
# )

# Inserindo Livro
# cursor.execute(
#     """
#     INSERT INTO Livros (livro_id, titulo,  editora_id, max_renovacoes)
#     VALUES
#     (1, 'Orientação a Objetos na Prática', 1, 3),
#     (2, 'Desenvolvendo CSS na Web', 2, 1),
#     (3, 'Dom Casmurro', 3, 4),
#     (4, 'A Hora da Estrela', 2, 3);
#     """
# )

# Criando a Tabela Exemplares
# cursor.execute(
#     """
#     CREATE TABLE Exemplares (
#     exemplar_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     livro_id INTEGER,
#     codigo VARCHAR(50),
#     disponivel BOOLEAN DEFAULT 1,
#     FOREIGN KEY (livro_id) REFERENCES Livros(livro_id));
#     """
# )
# cursor.execute(
#     """
# ALTER TABLE Exemplares ADD COLUMN  estado VARCHAR(25);
# """
# )

# Criando a tabela Usuarios
# cursor.execute(
#     """
#     CREATE TABLE Usuarios (
#     usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome VARCHAR(100) NOT NULL,
#     telefone VARCHAR(15),
#     nacionalidade VARCHAR(50));
#     """
# )

# Criando a tabela Emprestimos
# cursor.execute(
#     """
# CREATE TABLE Emprestimos (
#     emprestimo_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     usuario_id INTEGER,
#     exemplar_id INTEGER,
#     data_emprestimo DATE,
#     data_devolucao DATE,
#     estado VARCHAR(25),
#     renovacoes INTEGER DEFAULT 0,
#     FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id),
#     FOREIGN KEY (exemplar_id) REFERENCES Exemplares(exemplar_id)
# );
# """
# )

# Criando tabela Livro e Autores
# cursor.execute(
#     """
# CREATE TABLE Livro_Autores (
#     livro_id INTEGER,
#     autor_id INTEGER,
#     PRIMARY KEY (livro_id, autor_id),
#     FOREIGN KEY (livro_id) REFERENCES Livros(livro_id),
#     FOREIGN KEY (autor_id) REFERENCES Autores(autor_id)
# );
# """
# )

# Inserindo Livro e Autores
# cursor.execute(
#     """
#     INSERT INTO Livro_Autores (livro_id, autor_id)
#     VALUES
#     (1, 1),
#     (2, 2),
#     (3, 3),
#     (4, 4);
#     """
# )

# Inserindo Exemplares
# cursor.execute(
#     """
#     INSERT INTO Exemplares (exemplar_id, livro_id,  codigo, disponivel)
#     VALUES
#     (1, 1, 'OOP001', 1),
#     (2, 1, 'OOP002', 1),
#     (3, 2, 'DCW001', 1),
#     (4, 3, 'DC001', 0),
#     (5, 4, 'HE001', 2);
#     """
# )

# Consulta
# todos os livros disponivel
# dado = cursor.execute(
#     """
#     SELECT Livros.titulo, Exemplares.codigo
#     FROM Livros
#     JOIN Exemplares ON Livros.livro_id = Exemplares.livro_id
#     WHERE Exemplares.disponivel = 1;

#     """
# )

# Encontrar todos os livros emprestados
# dado = cursor.execute(
#     """
#     SELECT Livros.titulo, Exemplares.codigo
#     FROM Emprestimos
#     JOIN Exemplares ON Emprestimos.exemplar_id = Exemplares.exemplar_id
#     JOIN Livros ON Exemplares.livro_id = Livros.livro_id
#     WHERE Emprestimos.estado = 'Pendente'
#     """
# )

# # Para acessar os resultados
# resultados = dado.fetchall()
# for linha in resultados:
#     print(linha)


conexao.commit()
conexao.close
