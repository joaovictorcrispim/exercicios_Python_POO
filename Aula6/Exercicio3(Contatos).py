class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def atualizar_telefone(self,telefone):
        self.telefone = telefone

    def atualizar_email(self, email):
        self.email = email

contato_1 = Contato("João", "48988527799", "joaovictor@email.com")
print(f"Contato: {contato_1.nome} \ntelefone: {contato_1.telefone} \nemail: {contato_1.email}")

contato_1.atualizar_email("joaovictorcrispim@email.com")
contato_1.atualizar_telefone("48988529977")
print(f"Contato: {contato_1.nome} \ntelefone: {contato_1.telefone} \nemail: {contato_1.email}")