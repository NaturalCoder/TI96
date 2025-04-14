class Receita():
    def exibir_receita(self):
        print(f"** {self.nome} **")
        print("Ingredientes:")
        for ing in self.ingredientes:
            print(f"- {ing}")
        print("\nModo de preparo:")
        print(self.modo_preparo)

# Uso
brownie = Receita("Brownie")
brownie.adicionar_ingrediente("Chocolate 70%")
brownie.modo_preparo = "Misture tudo e asse por 30min"
brownie.exibir_receita()  # Exibirá a receita formatada