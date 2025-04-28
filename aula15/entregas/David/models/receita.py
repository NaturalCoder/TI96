class Receita:
    def __init__(self, nome):
        self.nome = nome
        self.ingredientes = []
        self.modo_preparo = ""

    def adicionar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def exibir(self):
        return {
            "nome": self.nome,
            "ingredientes": self.ingredientes,
            "modo_preparo": self.modo_preparo
        }