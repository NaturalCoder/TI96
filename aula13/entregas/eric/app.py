import random, os
from tabulate import tabulate 
from datetime import datetime

class Aluno():
    def __init__(self, id, nome, pontos = 0, perguntas = 0):
        self.id = id
        self.nome = nome
        self.pontos = pontos
        self.perguntas = perguntas
        self.logs = []  

    
    def registrar_resposta(self, pontos): 
       # Registra a alteração no log antes de atualizar os pontos
       self.logs.append({
           'data_hora': datetime.now(),
           'pontos_antes' : self.pontos,
           'pontos_depois' : self.pontos + pontos 
          
       })

       self.pontos += pontos
       self.perguntas += 1
       return self.pontos

class Turma():
    def __init__(self, alunos : list[Aluno]):
        self.alunos = alunos

    def proximo(self):
        
        m_n_perguntas = 999999
        for aluno in self.alunos:
            aluno.perguntas < m_n_perguntas
            m_n_perguntas = aluno.perguntas

        while True:
            aluno = random.choice(self.alunos)
            if aluno.perguntas == m_n_perguntas:
                return aluno
    def listar(self) -> str:
        """Retorna uma tabela formatada com os alunos e seus pontos."""
        tabela = [[aluno.id, aluno.nome, aluno.pontos, aluno.perguntas] for aluno in self.alunos]
        return tabulate(tabela, headers=["ID", "Nome", "Pontos", "Perguntas"], tablefmt="grid")


 # <-- NOVO MÉTODO ADICIONADO PARA MOSTRAR LOGS
    def mostrar_logs(self):
        """Retorna uma tabela com todos os logs de alteração de pontos"""
        logs_todos_alunos = []
        for aluno in self.alunos:
            for log in aluno.logs:
                logs_todos_alunos.append([
                    aluno.id,
                    aluno.nome,
                    log['data_hora'].strftime("%d/%m/%Y %H:%M:%S"),
                    log['pontos_antes'],
                    log['pontos_depois'],
                ])
        
        # Ordena do mais antigof para o mais novo ------>
        logs_todos_alunos.sort(key=lambda x: x[2], reverse=True)
        
        return tabulate(
            logs_todos_alunos,
            headers=["ID", "Nome", "Data/Hora", "Pontos Antes", "Pontos Adicionados", "Pontos Depois"],
            tablefmt="grid"
        )


list_alunos = [
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
    ]     

t = Turma(list_alunos)



#looping que pergunta, registra e mostra
while True :
    os.system('cls')
    print("1 - Próxima pergunta")  
    print("2 - Ver logs de alterações")
    print("0 - Sair")

    opcao = input("Escolha uma opção\n ")

    if opcao == "1":
        os.system('cls')
        pa = t.proximo()
        print(f"Pergunta a {pa.nome}")
        pontos = int(input("Resposta correta?\n1 Parcial, 2 Total, 0 Incorreta\nQuantos pontos:\n"))
        pa.registrar_resposta(pontos)

    resposta = input(f"Perguntar novamente? S/N\n ") 
    if resposta.lower() == 'n' :
        continue

    elif opcao == "2": 
     os.system('cls')
     print(t.mostrar_logs())
     input("\nPresione Enter para continuar...\n ")


    elif opcao == "0":
     os.system('cls')
     print("Finalizando")
     print(t.listar())
     break