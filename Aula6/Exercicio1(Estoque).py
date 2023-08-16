class Produto:
    def __init__(self, nome, preco: float, qtd_estoque: int):
        self.nome = nome
        self.preco = preco
        self.qtd_estoque = qtd_estoque


    def adicionar (self, quantidade: int):
        if quantidade > 0:
            self.qtd_estoque += quantidade
        else:
            print("Digite um valor válido")

    def remover(self, quantidade: int):
        if 0 < quantidade <= self.qtd_estoque:
            self.qtd_estoque -= quantidade
        else:
            print("Digite um valor válido")

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def valor_estoque(self):
        valor_total = 0
        for i in self.produtos:
            valor_total += float(i.preco) * float(i.qtd_estoque)
        return valor_total

estoque_1 = Estoque()
produto_1 = Produto("Calça", 100, 20)
produto_2 = Produto("Camiseta", 60, 50)
produto_3 = Produto("Meia", 10, 30)
produto_4 = Produto("Moletom", 160, 10)

estoque_1.adicionar_produto(produto_1)
estoque_1.adicionar_produto(produto_2)
estoque_1.adicionar_produto(produto_3)
estoque_1.adicionar_produto(produto_4)
print(f"Valor total em estoque: {estoque_1.valor_estoque()} R$")