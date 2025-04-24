class Receita():
    def __init__(self, nome):
        """Inicializa a receita com nome, ingredientes e modo de preparo."""
        self.nome = nome
        self.ingredientes = []
        self.modo_preparo = []

    def adicionar_ingrediente(self, ingrediente):
        """Adiciona um ingrediente à lista de ingredientes da receita."""
        self.ingredientes.append(ingrediente)



    def exibir_receita(self):
        """Exibe a receita formatada com ingredientes e modo de preparo."""
        print(f"** {self.nome} **")
        print("Ingredientes:")
        for ing in self.ingredientes:
            print(f"- {ing}")
        print("\nModo de preparo:")
        for i, etapa in enumerate(self.modo_preparo, 1):
            print(f"{i}. {etapa}")

class Menu():
    def __init__(self):
        """Inicializa o menu e a lista de receitas."""
        self.receitas = []

    def cadastrar_receita(self):
        """Método para cadastrar uma nova receita com múltiplas etapas de preparo."""
        nome = input("Digite o nome da receita: ")
        receita = Receita(nome)
        while True:
            ingrediente = input("Digite um ingrediente (ou 'fim' para terminar): ")
            if ingrediente.lower() == 'fim':
                break
            receita.adicionar_ingrediente(ingrediente)
        
        print("Agora vamos cadastrar o modo de preparo.")
        while True:
            etapa = input("Digite uma etapa do modo de preparo (ou 'fim' para terminar): ")
            if etapa.lower() == 'fim':
                break
            receita.adicionar_modo_preparo(etapa)
        
        self.receitas.append(receita)
        print(f"Receita {nome} cadastrada com sucesso!")

    def listar_receitas(self):
        """Método para listar todas as receitas cadastradas."""
        if not self.receitas:
            print("Não há receitas cadastradas.")
            return
        print("Receitas cadastradas:")
        for i, receita in enumerate(self.receitas, 1):
            print(f"{i}. {receita.nome}")

    def mostrar_receita(self):
        """Método para mostrar uma receita específica."""
        self.listar_receitas()
        escolha = int(input("Digite o número da receita que você quer ver: ")) - 1
        if 0 <= escolha < len(self.receitas):
            self.receitas[escolha].exibir_receita()
        else:
            print("Opção inválida!")

    def excluir_receita_por_indice(self):
        """Exclui a receita com base no índice fornecido pelo usuário."""
        self.listar_receitas()
        try:
            indice = int(input("Digite o número da receita que você deseja excluir: ")) - 1
            if 0 <= indice < len(self.receitas):
                removed = self.receitas.pop(indice)
                print(f"A receita '{removed.nome}' foi excluída com sucesso!")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

    def excluir_receita_por_nome(self):
        """Exclui a receita com base no nome fornecido pelo usuário."""
        nome = input("Digite o nome da receita que você deseja excluir: ")
        for receita in self.receitas:
            if receita.nome.lower() == nome.lower():
                self.receitas.remove(receita)
                print(f"A receita '{nome}' foi excluída com sucesso!")
                return
        print(f"Receita '{nome}' não encontrada.")

    def menu(self):
        """Exibe o menu e executa as ações de acordo com a escolha do usuário."""
        while True:
            print("\n*** Menu de Receitas ***")
            print("1. Cadastrar Receita")
            print("2. Listar Receitas")
            print("3. Mostrar Receita")
            print("4. Excluir Receita por Índice")
            print("5. Excluir Receita por Nome")
            print("6. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.cadastrar_receita()
            elif opcao == '2':
                self.listar_receitas()
            elif opcao == '3':
                self.mostrar_receita()
            elif opcao == '4':
                self.excluir_receita_por_indice()
            elif opcao == '5':
                self.excluir_receita_por_nome()
            elif opcao == '6':
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")


# Uso
menu = Menu()
menu.menu()