class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor
        self.velocidade = 0
 
    def acelerar(self):
        self.velocidade += 10
 
    def mostrar_velocidade(self, fim):
        print(f"A velocidade atual do {self.marca} é {self.velocidade} km/h.")
 
meu_carro = Carro("Fiat","Preto")
meu_carro.acelerar()
meu_carro.acelerar()
meu_carro.mostrar_velocidade("atual")