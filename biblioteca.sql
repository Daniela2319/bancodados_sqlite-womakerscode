CREATE TABLE Autores (
    autor_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    nacionalidade VARCHAR(50)
);

CREATE TABLE Editoras (
    editora_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE Livros (
    livro_id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(200) NOT NULL,
    editora_id INT,
    max_renovacoes INT,
    FOREIGN KEY (editora_id) REFERENCES Editoras(editora_id)
);

CREATE TABLE Exemplares (
    exemplar_id INT PRIMARY KEY AUTO_INCREMENT,
    livro_id INT,
    codigo VARCHAR(50),
    disponivel BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (livro_id) REFERENCES Livros(livro_id)
);

CREATE TABLE Usuarios (
    usuario_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(15),
    nacionalidade VARCHAR(50)
);

CREATE TABLE Emprestimos (
    emprestimo_id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT,
    exemplar_id INT,
    data_emprestimo DATE,
    data_devolucao DATE,
    estado VARCHAR(20),
    renovacoes INT DEFAULT 0,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id),
    FOREIGN KEY (exemplar_id) REFERENCES Exemplares(exemplar_id)
);

CREATE TABLE Livros_Autores (
    livro_id INT,
    autor_id INT,
    PRIMARY KEY (livro_id, autor_id),
    FOREIGN KEY (livro_id) REFERENCES Livros(livro_id),
    FOREIGN KEY (autor_id) REFERENCES Autores(autor_id)
);