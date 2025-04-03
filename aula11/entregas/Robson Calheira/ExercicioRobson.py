# Criando classe carro
class Carro:
    def __init__(self, cor, marca):
        self.cor = cor
        self.marca = marca

    def andar(self):
        print(f"{self.cor} {self.marca}: Andei")

# Criando classe CarroElétrico
class CarroEletrico(Carro):
    def __init__(self, cor, marca, velocidade=0):      
        super().__init__(cor, marca)  # Chama o construtor da classe Carro
        self.velocidade = int(velocidade)
        self.bateria = 100
    
    def acelerar(self):
        if self.bateria > 0:
            consumo = 5  # Consumo base
            
            if self.velocidade >= 50 and self.velocidade < 100:
                consumo = 10
            elif self.velocidade >= 100:
                consumo = 15

            if self.bateria >= consumo:
                self.velocidade += 10
                self.bateria -= consumo
                print(f"{self.marca} acelerou para {self.velocidade} km/h. Bateria restante: {self.bateria}%")
            else:
                print("Bateria fraca! Recarregue.")
        else:
            print("Bateria zerada! O carro não pode acelerar.")

    def set_velocidade(self, velocidade):
        self.velocidade = velocidade

    def mostrar_bateria(self):
        print(f"Bateria restante: {self.bateria}%")

# Exemplo de uso:
carro_eletrico = CarroEletrico('Preto', 'Polo')

# Testando múltiplas acelerações
carro_eletrico.acelerar()
carro_eletrico.acelerar()
carro_eletrico.acelerar()
carro_eletrico.acelerar()
carro_eletrico.acelerar()
carro_eletrico.mostrar_bateria()
