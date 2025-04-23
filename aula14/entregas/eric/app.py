class Receita():
    def __init__(self, nome, ingredientes, modo_preparo):
        self.nome = nome
        self.ingredientes = ingredientes
        self.modo_preparo = modo_preparo

    def exibir_receita(self):
        print(f"** {self.nome} **")
        print("Ingredientes:")
        for i in self.ingredientes:
            print(f"- {i}")
        print("\nModo de preparo:")
        print(self.modo_preparo)

def cadastrar_receita():
    nome = input("Digite o nome da receita: ")
    ingredientes = []
    print("Digite os ingredientes (digite 'fim' para parar):")
    while True:
        ingrediente = input("- ")
        if ingrediente.lower() == 'fim':
            break
        ingredientes.append(ingrediente)
    modo_preparo = input("Digite o modo de preparo: ")
    return Receita(nome, ingredientes, modo_preparo)

def listar_receitas(receitas):
    if not receitas:
        print("Nenhuma receita cadastrada.")
    else:
        print("\nReceitas cadastradas:")
        for i, receita in enumerate(receitas, 1):
            print(f"{i}. {receita.nome}")

def mostrar_receita(receitas):
    listar_receitas(receitas)
    if receitas:
        try:
            num = int(input("\nDigite o número da receita que deseja ver: ")) - 1
            if 0 <= num < len(receitas):
                print()
                receitas[num].exibir_receita()
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor, digite um número válido.")

def main():
    receitas = []
    while True:
        print("\n=== MENU DE RECEITAS ===")
        print("1. Cadastrar nova receita")
        print("2. Listar receitas cadastradas")
        print("3. Mostrar a receita")
        print("4. Finalizar Código")
        
        opcao = input("Escolha a opção desejada: ")
        
        if opcao == '1':
            receitas.append(cadastrar_receita())
            print("Receita cadastrada!")
        elif opcao == '2':
            listar_receitas(receitas)
        elif opcao == '3':
            mostrar_receita(receitas)
        elif opcao == '4':
            print("Finalizando programa")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()