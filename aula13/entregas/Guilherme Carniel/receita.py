# Definição completa da classe Receita
class Receita:
    def __init__(self, nome):
        self.nome = nome  # Nome da receita
        self.ingredientes = []  # Lista de ingredientes
        self.modo_preparo = ""  # Modo de preparo

    def adicionar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)  # Adiciona ingrediente à lista

    def definir_modo_preparo(self, texto):
        self.modo_preparo = texto  # Define o modo de preparo

    def exibir_receita(self):
        print(f"\n== {self.nome} ==")
        print("Ingredientes:")
        for ing in self.ingredientes:
            print(f"- {ing}")
        print("\nModo de preparo:")
        print(self.modo_preparo)

# Lista para armazenar receitas cadastradas no menu
receitas = []

# Exemplo de uso direto (teste individual de uma receita)
brownie = Receita("Brownie")
brownie.adicionar_ingrediente("Chocolate 70%")
brownie.adicionar_ingrediente("Ovos")
brownie.adicionar_ingrediente("Açúcar")
brownie.adicionar_ingrediente("Farinha de trigo")
brownie.definir_modo_preparo("Misture tudo e asse por 30 minutos a 180 graus.")
receitas.append(brownie)  # Adiciona o brownie à lista usada no menu

# Menu interativo
while True:
    print("\n===== MENU DE RECEITAS =====")
    print("1. Cadastrar nova receita")
    print("2. Listar receitas cadastradas")
    print("3. Mostrar detalhes de uma receita")
    print("4. Encerrar programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome da receita: ")
        receita = Receita(nome)

        print("Digite os ingredientes (digite 'fim' para encerrar):")
        while True:
            ingrediente = input("- ")
            if ingrediente.lower() == "fim":
                break
            receita.adicionar_ingrediente(ingrediente)

        preparo = input("Digite o modo de preparo: ")
        receita.definir_modo_preparo(preparo)

        receitas.append(receita)
        print("Receita cadastrada com sucesso.")

    elif opcao == "2":
        if not receitas:
            print("Nenhuma receita cadastrada.")
        else:
            print("\nLista de receitas:")
            for i, r in enumerate(receitas):
                print(f"{i + 1}. {r.nome}")

    elif opcao == "3":
        if not receitas:
            print("Nenhuma receita cadastrada.")
        else:
            while True:
                print("\nLista de receitas:")
                for i, r in enumerate(receitas):
                    print(f"{i + 1}. {r.nome}")
                print("0. Voltar ao menu principal")

                try:
                    escolha = int(input("Digite o número da receita que deseja ver: "))
                    if escolha == 0:
                        break  # Retorna ao menu principal
                    elif 1 <= escolha <= len(receitas):
                        receitas[escolha - 1].exibir_receita()
                        input("\nPressione Enter para continuar...")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Digite um número válido.")

