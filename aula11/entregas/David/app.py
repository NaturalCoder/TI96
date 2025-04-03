class Carro:
    def __init__(self, marca: str):
        self.marca = marca
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

    def mostrar_velocidade(self):
        print(f"Velocidade atual: {self.velocidade} km/h")
