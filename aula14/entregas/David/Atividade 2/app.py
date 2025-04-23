class Receita:
    def __init__(self, nome):
        self.nome = nome
        self.ingredientes = []
        self.modo_preparo = ""

    def adicionar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def exibir_receita(self):
        print(f"\n** {self.nome} **")
        print("Ingredientes:")
        for i in self.ingredientes:
            print(f"- {i}")
        print("Modo de preparo:")
        print(self.modo_preparo)
        print("-" * 30)

def cadastrar_receita(receitas):
    nome = input("Nome da receita: ").strip()
    if not nome:
        print("Nome não pode ser vazio!\n")
        return
    receita = Receita(nome)
    print("Digite os ingredientes (vazio para terminar):")
    while True:
        ing = input("Ingrediente: ").strip()
        if not ing:
            break
        receita.adicionar_ingrediente(ing)
    receita.modo_preparo = input("Modo de preparo: ").strip()
    receitas.append(receita)
    print("Receita cadastrada com sucesso!\n")

def listar_receitas(receitas):
    if not receitas:
        print("Nenhuma receita cadastrada.\n")
        return
    print("\nReceitas cadastradas:")
    for idx, r in enumerate(receitas):
        print(f"{idx + 1}. {r.nome}")
    print()

def mostrar_receita(receitas):
    if not receitas:
        print("Nenhuma receita cadastrada.\n")
        return
    listar_receitas(receitas)
    try:
        idx = int(input("Digite o número da receita para exibir: ")) - 1
        if 0 <= idx < len(receitas):
            receitas[idx].exibir_receita()
        else:
            print("Índice inválido.\n")
    except ValueError:
        print("Entrada inválida.\n")

def menu():
    receitas = []
    while True:
        print("1. Cadastrar receita")
        print("2. Listar receitas")
        print("3. Mostrar receita")
        print("4. Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_receita(receitas)
        elif opcao == "2":
            listar_receitas(receitas)
        elif opcao == "3":
            mostrar_receita(receitas)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    menu()