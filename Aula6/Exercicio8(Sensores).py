class Sensor:
    def __init__(self, identificador, unidade_de_medida, temperatura_atual: float):
        self.identificador = identificador
        self.unidade_de_medida  = unidade_de_medida
        self.temperatura_atual = temperatura_atual

    def atualizar_temperatura(self, temperatura):
        self.temperatura_atual = temperatura

    def leitura_atual(self):
        print(f"Sensor: {self.identificador}\nTemperatura: {self.temperatura_atual} {self.unidade_de_medida}")

sensor = Sensor("Sen123", "ºC", 24.5)
sensor.leitura_atual()
sensor.atualizar_temperatura(22.3)
sensor.leitura_atual()
