class Passageiro:
    def __init__(self, nome, numero_passaporte):
        self.nome = nome
        self.numero_passaporte = numero_passaporte

class Voo:
    def __init__(self, numero_voo, origem, destino, capacidade_maxima: int):
        self.numero_voo = numero_voo
        self.origem = origem
        self.destino = destino
        self.capacidade_maxima = capacidade_maxima
        self.reservas = []

    def verificar_lotacao(self):
        if self.reservas.__len__() == self.capacidade_maxima:
            print("Voo lotado, não é mais possivel realizar reservas")
            return True
        else:
            print(f"Assentos disponíveis { self.capacidade_maxima - self.reservas.__len__() }")
            return False

    def reservar_assento(self, passageiro):
        if self.verificar_lotacao() is False:
            reserva = Reserva(passageiro, self)
            self.reservas.append(reserva)

    def listar_reservas(self):
        print(f"Voo: {self.numero_voo}")
        print("Lista de reservas:")
        for i in self.reservas:
            print(i.passageiro.nome)


class Reserva:
    def __init__(self, passageiro: Passageiro, voo: Voo):
        self.passageiro = passageiro
        self.voo = voo


voo = Voo("123", "Florianópolis", "São Paulo", 5)
passageiro_1 = Passageiro("João", "123456")
passageiro_2 = Passageiro("Maria", "546987")
passageiro_3 = Passageiro("Fernando", "156987")
passageiro_4 = Passageiro("Victor", "654321")
passageiro_5 = Passageiro("Lucas", "741852")
passageiro_6 = Passageiro("Rafael", "147258")

voo.reservar_assento(passageiro_1)
voo.reservar_assento(passageiro_2)
voo.reservar_assento(passageiro_3)
voo.reservar_assento(passageiro_4)
voo.reservar_assento(passageiro_5)
voo.verificar_lotacao()
voo.listar_reservas()

voo.reservar_assento(passageiro_6)