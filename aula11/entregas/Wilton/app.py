class Carro:
    def __init__(self, marca, velocidade = 0):
        self.marca = marca
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 10

    def mostrar_velocidade(self):
        print(f"A velocidade atual do {self.marca} é {self.velocidade} km/h")

meu_carro = Carro("Toyota", 90)
meu_carro.acelerar()
meu_carro.acelerar()
meu_carro.mostrar_velocidade()



class CarroEletrico(Carro):
    def __init__(self, marca):
        super().__init__(marca)
        self.bateria = 10

    def acelerar(self):
        if self.bateria >= 10:
            self.velocidade += 10
            self.bateria -= 5
        else:
            print("Bateria muito baixa para acelerar!")

    def mostrar_status(self):
        print(f"A velocidade atual do {self.marca} e {self.velocidade} km/h | Bateria: {self.bateria}%")

carro_eletrico = CarroEletrico("Tesla")
carro_eletrico.acelerar()
carro_eletrico.acelerar()
carro_eletrico.mostrar_status()