import random, os
from tabulate import tabulate
 
class Aluno():
    def __init__(self, id, nome, pontos=0, perguntas=0):
        self.id = id
        self.nome = nome
        self.pontos = pontos
        self.perguntas = perguntas
 
    def registrar_resposta(self, pontos):
        self.pontos += pontos
        self.perguntas += 13
        return self.pontos
 
class Turma():
    def __init__(self, alunos: list[Aluno]):
        self.alunos = alunos
        self.logs = []  # Lista para armazenar os logs
 
    def proximo(self):
        m_n_perguntas = min(aluno.perguntas for aluno in self.alunos)
        candidatos = [aluno for aluno in self.alunos if aluno.perguntas == m_n_perguntas]
        return random.choice(candidatos)
 
    def listar(self) -> str:
        """Retorna uma tabela formatada com os alunos e seus pontos."""
        tabela = [[aluno.id, aluno.nome, aluno.pontos, aluno.perguntas] for aluno in self.alunos]
        return tabulate(tabela, headers=["ID", "Nome", "Pontos", "Perguntas"], tablefmt="grid")
 
    def mostrar_logs(self) -> str:
        if not self.logs:
            return "Nenhum log registrado ainda."
        tabela_logs = tabulate(self.logs, headers=["ID", "Nome", "Pontos Recebidos", "Total de Perguntas"], tablefmt="grid")
        return tabela_logs
 
# Lista de alunos
list_alunos = [
    Aluno(id=0, nome="Alisson do Nascimento Junior"),
    Aluno(id=1, nome="Daiane da Silva Lourenço"),
    Aluno(id=2, nome="David Gomes de Freitas"),
    Aluno(id=3, nome="Emerson Domingues Prado"),
    Aluno(id=4, nome="Eric Barbosa Costa"),
    Aluno(id=5, nome="Evandro Antonio Gerola"),
    Aluno(id=6, nome="Felipe Souza de Araujo"),
    Aluno(id=7, nome="Guilherme Carniel"),
    Aluno(id=8, nome="Iann Silva Ferreira"),
    Aluno(id=9, nome="João Antonio Ribeiro do Nascimento"),
    Aluno(id=10, nome="João Luis Santana Cavalcante"),
    Aluno(id=11, nome="João Vitor Piemonte dos Santos"),
    Aluno(id=12, nome="Pamella Ribeiro de Barros"),
    Aluno(id=13, nome="Ramon da Silva Servio"),
    Aluno(id=14, nome="Regiane Maria Rosa Castro"),
    Aluno(id=15, nome="Robson Calheira dos Santos"),
    Aluno(id=16, nome="Rodrigo Faria de Souza"),
    Aluno(id=17, nome="Valkíria de Sena Santos"),
    Aluno(id=18, nome="Valter André da Costa"),
    Aluno(id=19, nome="Victor Henrique Rossi Mazete"),
    Aluno(id=20, nome="Wilton Ferreira do Nascimento")
]
 
#criando turma
t = Turma(list_alunos)
 
#loop com menu
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== MENU ===")
    print("1. Fazer pergunta")
    print("2. Ver ranking")
    print("3. Ver logs")
    print("0. Sair")
    escolha = input("Escolha uma opção: ")
 
    if escolha == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        pa = t.proximo()
        print(f"Pergunta para: {pa.nome}")
        pontos = int(input("Resposta correta?\n1 Parcial, 2 Total, 0 Incorreta\nQuantos pontos: "))
        pa.registrar_resposta(pontos)
        t.logs.append([pa.id, pa.nome, pontos, pa.perguntas])
        input("\nPressione ENTER para voltar ao menu...")
    elif escolha == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== Ranking de Pontuação ===")
        print(t.listar())
        input("\nPressione ENTER para voltar ao menu...")
    elif escolha == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== Logs de Respostas ===")
        print(t.mostrar_logs())
        input("\nPressione ENTER para voltar ao menu...")
    elif escolha == "0":
        print("Finalizando programa...")
        break
    else:
        print("Opção inválida.")
        input("\nPressione ENTER para tentar novamente...")