class Receita:
    def __init__(self, nome):
        self.nome = nome
        self.ingredientes = []
        self.modo_preparo = ""

    def adicionar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def exibir(self):
        print(f"\n== {self.nome} ==")
        print("Ingredientes:")
        for item in self.ingredientes:
            print(f"- {item}")
        print("\nModo de preparo:")
        print(self.modo_preparo)


def main():
    receitas = []

    while True:
        print("\nMenu de Receitas")
        print("1 - Nova receita")
        print("2 - Ver receitas salvas")
        print("3 - Ver detalhes de uma receita")
        print("4 - Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            nome = input("Nome da receita: ")
            nova = Receita(nome)

            print("Digite os ingredientes (digite 'fim' para encerrar):")
            while True:
                ing = input("- ")
                if ing.lower() == "fim":
                    break
                nova.adicionar_ingrediente(ing)

            nova.modo_preparo = input("Modo de preparo: ")
            receitas.append(nova)
            print("Receita adicionada com sucesso!")

        elif opcao == "2":
            if not receitas:
                print("Nenhuma receita até agora.")
            else:
                print("Receitas cadastradas:")
                for i, r in enumerate(receitas):
                    print(f"{i + 1} - {r.nome}")

        elif opcao == "3":
            if not receitas:
                print("Nenhuma receita cadastrada.")
            else:
                try:
                    indice = int(input("Número da receita: ")) - 1
                    if 0 <= indice < len(receitas):
                        receitas[indice].exibir()
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Por favor, digite um número válido.")

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()