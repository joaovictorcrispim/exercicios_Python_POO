class Tarefa:
    def __init__(self, descricao, data_de_criacao):
        self.descricao = descricao
        self.data_de_criacao = data_de_criacao
        self.status = False

    def concluir_tarefa(self):
        self.status = True

    def detalhes_tarefa(self):
        status = "Em andamento"
        if self.status == True:
            status = "concluido"
        print(f"Tarefa: {self.descricao} \nCrição: {self.data_de_criacao} \nStatus {status}")

tarefa = Tarefa("Fazer lista de exercicios", "15/08/2023")
tarefa.detalhes_tarefa()

tarefa.concluir_tarefa()
tarefa.detalhes_tarefa()
