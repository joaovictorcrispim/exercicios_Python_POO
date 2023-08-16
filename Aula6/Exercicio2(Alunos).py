class Aluno:
    def __init__(self, nome, idade: int):
        self.nome = nome
        self.idade = idade
        self.disciplinas = []

    def adicionar_disicplinas(self, disciplina):
        self.disciplinas.append(disciplina)

    def disciplinas_cursadas(self):
        for i in self.disciplinas:
            print(i)

aluno_1 = Aluno("João", 23)
aluno_1.adicionar_disicplinas("SGBD")
aluno_1.adicionar_disicplinas("POO")
aluno_1.adicionar_disicplinas("Analise de requisitos")
aluno_1.adicionar_disicplinas("Fundamentos da pesquisa")
print(f"Disciplinas cursadas pelo aluno {aluno_1.nome}: ")
aluno_1.disciplinas_cursadas()