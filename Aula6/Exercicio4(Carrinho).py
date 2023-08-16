class carrinho_de_compras:
    def __init__(self):
        self.produtos = []
        self.precos = []

    def adicionar_produtos(self, produto, preco: float):
        self.produtos.append(produto)
        self.precos.append(preco)

    def total_da_compra(self):
        return sum(self.precos)

    def produtos_carrinho(self):
        print('Produtos:')
        for i in self.produtos:
            print(i)

carrinho = carrinho_de_compras()
carrinho.adicionar_produtos("calça", 100)
carrinho.adicionar_produtos("camiseta", 80)
carrinho.adicionar_produtos("meia", 10)
carrinho.adicionar_produtos("moletom", 160)

carrinho.produtos_carrinho()
print(f"Valor total do carrinho: {carrinho.total_da_compra()} R$")