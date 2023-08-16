class Livro:
    def __init__(self, titulo, autor, ano_publicacao: int, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero

    def atualizar_ano_publicacao(self, ano):
        self.ano_publicacao = ano

    def detalhes_livro(self):
        print(f"Livro: {self.titulo}\nAutor: {self.autor}\nPublicado em: {self.ano_publicacao}\nGênero: {self.genero}")

livro = Livro("O nome do vento", "Patrick Rothfuss", 2009, "Ficção")
livro.detalhes_livro()
livro.atualizar_ano_publicacao(2007)
livro.detalhes_livro()
