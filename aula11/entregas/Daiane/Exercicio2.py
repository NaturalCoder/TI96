class Carro:
    def __init__(self, marca):
        self.marca = marca
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

    def mostrar_velocidade(self):
        print(f"Velocidade: {self.velocidade} km/h")


class CarroEletrico(Carro):
    def __init__(self, marca):
        super().__init__(marca)
        self.bateria = 100

    def acelerar(self):
        if self.bateria >= 10:
            self.velocidade += 10
            self.bateria -= 5
        else:
            print("Bateria baixa! Não é possível acelerar.")

    def mostrar_bateria(self):
        print(f"Bateria: {self.bateria}%")

# Exemplo de uso
carro_eletrico = CarroEletrico("Tesla")
carro_eletrico.mostrar_velocidade()
carro_eletrico.mostrar_bateria()
carro_eletrico.acelerar()
carro_eletrico.mostrar_velocidade()
carro_eletrico.mostrar_bateria()