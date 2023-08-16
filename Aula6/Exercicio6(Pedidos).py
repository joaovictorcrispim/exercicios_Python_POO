class Pedido:
    def __init__(self, numero: int, data):
        self.numero = numero
        self.data = data
        self.itens = []

    def adicionar_itens(self, item):
        self.itens.append(item)

pedido = Pedido(23, "15/08/2023")
pedido.adicionar_itens("coca-cola")
pedido.adicionar_itens("x-burguer")
pedido.adicionar_itens("milkshake")
print(f"Pedido: {pedido.numero} \n itens: {pedido.itens}")