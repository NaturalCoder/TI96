class Carro:
    def __init__(self, marca, velocidade = 0):
        self.marca = marca
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade = self.velocidade + 10

    def mostrar_velocidade(self):
        print(f"Sua velocidade atual é de {self.velocidade}")