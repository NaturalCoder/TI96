class Receita:
    def __init__(self):
        self.receitas = []  # Lista de receitas

    def cadastrar(self):
        print("\nCadastro de nova receita:")
        nome = input("Nome da receita: ")
        ingredientes = input("Ingredientes (separados por vírgula): ")
        modo_preparo = input("Modo de preparo: ")
        self.receitas.append({
            "nome": nome.strip(),
            "ingredientes": [i.strip() for i in ingredientes.split(",")],
            "modo_preparo": modo_preparo.strip()
        })
        print("Receita cadastrada com sucesso.\n")

    def listar(self):
        if not self.receitas:
            print("Nenhuma receita cadastrada.\n")
            return
        print("\nLista de receitas:")
        for i, r in enumerate(self.receitas):
            print(f"{i + 1}. {r['nome']}")
        print()

    def mostrar(self):
        if not self.receitas:
            print("Nenhuma receita cadastrada.\n")
            return
        try:
            indice = int(input("Digite o número da receita que deseja ver: ")) - 1
            r = self.receitas[indice]
            print(f"\nReceita: {r['nome']}")
            print("Ingredientes:")
            for ing in r['ingredientes']:
                print(f" - {ing}")
            print(f"\nModo de preparo:\n{r['modo_preparo']}\n")
        except (IndexError, ValueError):
            print("Número inválido. Tente novamente.\n")


# Instanciando e iniciando o menu de receitas
livro_receitas = Receita()

while True:
    print("\n===== MENU DE RECEITAS =====")
    print("1. Cadastrar nova receita")
    print("2. Listar receitas cadastradas")
    print("3. Mostrar detalhes de uma receita")
    print("4. Encerrar programa")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        livro_receitas.cadastrar()
    elif opcao == "2":
        livro_receitas.listar()
    elif opcao == "3":
        livro_receitas.mostrar()
    elif opcao == "4":
        print("Encerrando o programa. Até mais.")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
