class Carro:
    def __init__(self, marca, cor, velocidade = 0):
        self.marca = marca
        self.cor = cor
        self.velocidade = int(velocidade)

    def acelerar (self):
        self.velocidade += 10
    def mostrar_vel (self):
        print(f"{self.marca}, {self.cor}, {self.velocidade}km/h!")

Fusca = Carro ("Volkswagem", "Azul", "50")
Jeep = Carro("Jeep", "Preto")

print (Fusca.marca)

Jeep.acelerar()
Fusca.mostrar_vel()
Jeep.mostrar_vel()

#class CarroEletrico(Carro):
#    def __init__(self, marca, cor, velocidade = 0, bateria = 100):
#        super().__init__(self, marca, cor, velocidade)
#        self.bateria = int(bateria)
#    def acelerar(self):
#        if self.bateria >= 10:
#            while (self.bateria >= 10):
#                self.bateria -= 5
#                self.velocidade += 10
#                print({self.bateria})
#        else:
#           print("5% de bateria! Por favor, recarregue!")
#
#Audi = Carro ("Audi")