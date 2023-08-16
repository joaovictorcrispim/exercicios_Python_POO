class conta_bancaria:
    def __init__(self, numero: int, titular, saldo: float):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor inválido")

conta = conta_bancaria(565, "João", 1350)
conta.depositar(3520)
print(f"Saldo: {conta.saldo} R$")