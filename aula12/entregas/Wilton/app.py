import random

class Aluno:
    def __init__(self, id: int, nome: str, pontos: int = 0, perguntas: int = 0):
        self.id = id
        self.nome = nome
        self.pontos = pontos
        self.perguntas = perguntas

    def registrar_resposta(self, pontos: int) -> bool:
        """
        Registra a resposta do aluno, adicionando pontos ao total.
        :param pontos: Pontuação da resposta (0 - incorreta, 1 - parcial, 2 - total).
        """
        if pontos in [0, 1, 2]:
            self.pontos += pontos
            self.perguntas += 1
            return True
        else:
            return False

class Turma:
    def __init__(self, alunos: list):
        self.alunos = alunos
        self.alunos_selecionados = []  # Lista para armazenar os alunos já selecionados

    def proximo(self) -> Aluno:
        """
        Retorna um aluno aleatório a responder, sem repetir o mesmo aluno consecutivamente.
        :return: O próximo aluno aleatório.
        """
        # Se todos os alunos já foram selecionados, reinicia o ciclo
        if len(self.alunos_selecionados) == len(self.alunos):
            self.alunos_selecionados = []

        # Escolhe um aluno aleatório, mas que ainda não foi selecionado
        aluno = random.choice([a for a in self.alunos if a not in self.alunos_selecionados])

        # Adiciona o aluno à lista de selecionados
        self.alunos_selecionados.append(aluno)
        return aluno

    def listar(self) -> str:
        """
        Retorna uma lista com os alunos e seus pontos.
        :return: String formatada com alunos e pontos.
        """
        lista_alunos = "\n".join([f"{aluno.nome}: {aluno.pontos} pontos" for aluno in self.alunos])
        return lista_alunos


# Criação dos objetos de alunos e turma
t = Turma([
    Aluno(id=0, nome="Alisson do Nascimento Junior"),
    Aluno(id=1 , nome="Daiane da Silva Lourenço"),
    Aluno(id=2 , nome="David Gomes de Freitas"),
    Aluno(id=3 , nome="Emerson Domingues Prado"),
    Aluno(id=4 , nome="Eric Barbosa Costa"),
    Aluno(id=5 , nome="Evandro Antonio Gerola"),
    Aluno(id=6 , nome="Felipe Souza de Araujo"),
    Aluno(id=7 , nome="Guilherme Carniel"),
    Aluno(id=8 , nome="Iann Silva Ferreira"),
    Aluno(id=9 , nome="João Antonio Ribeiro do Nascimento"),
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
])

# Laço de perguntas, registro de respostas e exibição de resultados
while True:
    pa = t.proximo()
    print(f"Pergunta a {pa.nome}")
    

    # Garantir que os pontos sejam um valor válido
    while True:
        pontos = input("Resposta correta? 1 Parcial, 2 Total, 0 Incorreta: ")
        if pa.registrar_resposta(int(pontos)):
            break

    resp = input(f"Perguntar novamente? S/N: ")
    if resp.upper() == "N":
        print("\nRanking dos Alunos:")
        print(t.listar())
        break


