#Este programa em Python simula uma dinâmica de perguntas em sala de aula, onde alunos são selecionados de forma justa com base na quantidade de vezes que já responderam. 
# A cada rodada, o sistema escolhe aleatoriamente entre os que têm menos participações e permite ao usuário registrar se a resposta foi incorreta, parcial ou totalmente 
# correta, atribuindo pontos conforme o desempenho. Ao final da atividade, uma tabela organizada exibe o nome de cada aluno, o número de perguntas respondidas e sua pontuação 
# acumulada, facilitando o acompanhamento da participação de todos.

import random, os  # Importa módulos: random (para sorteios) e os (não usado no código atual)
from tabulate import tabulate  # Importa função para formatar dados em tabelas
from datetime import datetime


# Classe que representa um aluno
class Aluno:
    def __init__(self, id, nome, pontos = 0, perguntas = 4):
        self.log = []  # Lista para armazenar o histórico de alterações de pontuação - EXERCICIO 1 - PARTE 1
        self.id = id  # ID do aluno
        self.nome = nome  # Nome do aluno
        self.pontos = pontos  # Pontos acumulados pelas respostas
        self.perguntas = perguntas  # Quantidade de vezes que já respondeu (default é 4)

    def registrar_resposta(self, pontos):
        self.pontos += pontos  # Atualiza os pontos totais
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Captura a data e hora atual
        self.log.append(f"[{agora}] +{pontos} ponto(s), total: {self.pontos}")  # Adiciona ao log

    def exibir_log(self): #EXERCICIO 1 - PARTE 1
        return "\n".join(self.log) if self.log else "Nenhum registro ainda."

# Classe que representa uma turma com vários alunos
class Turma:
    def __init__(self, alunos:list[Aluno]):
        self.alunos = alunos  # Recebe a lista de alunos

    def proximo(self):  # Escolhe o próximo aluno que vai responder
        menor_n_perg = 99999999999  # Começa com um número muito alto para encontrar o menor
        for aluno in self.alunos:  # Percorre todos os alunos
            if aluno.perguntas < menor_n_perg:  # Se o aluno respondeu menos vezes...
                menor_n_perg = aluno.perguntas  # ...atualiza o valor mínimo

        while True:  # Loop até achar um aluno com o menor número de perguntas
            aluno = self.alunos[random.randrange(0,20)]  # Escolhe um aluno aleatório (de 0 a 19)
            if aluno.perguntas == menor_n_perg:  # Se ele tiver o menor número de perguntas...
                aluno.perguntas += 1  # ...contabiliza mais uma pergunta para ele
                return aluno  # Retorna esse aluno para a rodada

    def listar(self):  # Define o método 'listar' da classe Turma, que irá exibir os dados dos alunos em formato de tabela.
        dados = [[aluno.id, aluno.nome, aluno.pontos, aluno.perguntas] for aluno in self.alunos]
        # Cria uma lista chamada 'dados', onde:
        # - Cada item da lista será outra lista com 4 elementos: [id, nome, pontos, perguntas]
        # - Essa estrutura é construída para cada 'aluno' presente na lista self.alunos
        # Resultado: uma tabela de dados com os atributos principais de cada aluno da turma.
        return tabulate(dados, headers=["ID", "Nome", "Pontos", "Perguntas"], tablefmt="fancy_grid")
        # A função 'tabulate' transforma a lista de listas (dados) em uma tabela formatada de texto.
        # 'headers' define os títulos das colunas.
        # 'tablefmt="fancy_grid"' define o estilo visual da tabela (com bordas e separadores).
        # A tabela gerada é retornada para ser exibida onde o método for chamado.

# Lista de alunos da turma
lista_alunos = [
    Aluno(id=0, nome="Alisson do Nascimento Junior"),
    Aluno(id=1 , nome="Daiane da Silva Lourenço", perguntas=3),
    Aluno(id=2 , nome="David Gomes de Freitas"),
    Aluno(id=3 , nome="Emerson Domingues Prado"),
    Aluno(id=4 , nome="Eric Barbosa Costa"),
    Aluno(id=5 , nome="Evandro Antonio Gerola"),
    Aluno(id=6 , nome="Felipe Souza de Araujo"),
    Aluno(id=7 , nome="Guilherme Carniel"),
    Aluno(id=8 , nome="Iann Silva Ferreira", perguntas=3),
    Aluno(id=9 , nome="João Antonio Ribeiro do Nascimento"),
    Aluno(id=10, nome="João Luis Santana Cavalcante"),
    Aluno(id=11, nome="João Vitor Piemonte dos Santos"),
    Aluno(id=12, nome="Pamella Ribeiro de Barros"),
    Aluno(id=13, nome="Ramon da Silva Servio"),
    Aluno(id=14, nome="Regiane Maria Rosa Castro", perguntas=3),
    Aluno(id=15, nome="Robson Calheira dos Santos"),
    Aluno(id=16, nome="Rodrigo Faria de Souza"),
    Aluno(id=17, nome="Valkíria de Sena Santos"),
    Aluno(id=18, nome="Valter André da Costa"),
    Aluno(id=19, nome="Victor Henrique Rossi Mazete"),
    Aluno(id=20, nome="Wilton Ferreira do Nascimento")
]

t = Turma(lista_alunos)  # Cria uma instância da turma com os alunos listados

# Loop de perguntas até o usuário digitar "N"
while True :
    pa = t.proximo()  # Seleciona o próximo aluno para responder
    print(f"Pergunta a {pa.nome}")  # Mostra o nome do aluno sorteado
    pontos = int(input("Resposta correta? 1 Parcial, 2 Total, 0 Incorreta: "))  # Pergunta pontuação
    pa.registrar_resposta(pontos)  # Registra os pontos ganhos pelo aluno

    resp = input(f"Perguntar novamente? S/N: ")  # Pergunta se deve continuar

    if resp == "N" or resp == "n":  # Se a resposta for N (não)...
        print(t.listar())  # Mostra a tabela final com os resultados
        break  # Encerra o loop

print("\nLOG DE ALTERAÇÕES DE PONTOS:") # LOG PARA PRINTAR - EXERCICIO 1 - PARTE 2
for aluno in lista_alunos:
    print(f"\n{aluno.nome}:")
    print(aluno.exibir_log())

# ================= EXERCÍCIO 2 – PARTE 1 e 2: CLASSE RECEITA COM MENU =================
