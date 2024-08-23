dado = cursor.execute(
#     """
#     SELECT Livros.titulo, Exemplares.codigo
#     FROM Emprestimos
#     JOIN Exemplares ON Emprestimos.exemplar_id = Exemplares.exemplar_id
#     JOIN Livros ON Exemplares.livro_id = Livros.livro_id
#     WHERE Emprestimos.estado = 'Pendente'
    
#     """
# )