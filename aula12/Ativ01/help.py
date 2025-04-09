class Aluno:
    def __init__(self, id, nome, pontos = 0, perguntas = 0):
        self.id = id
        self.nome = nome
        self.pontos = pontos
        self.perguntas = perguntas


class Turma:
    def __init__(self, alunos):
        self.alunos = alunos

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

#crie um metodo que retorne o proximo aluno a responder uma pergunta
#atenção apesar de esperar um aluno aleatório o mesmo aluno não pode ser chamado 
#duas vezes consecutivas até que seja circulado todos os alunos do grupo
#complete as anotações de tipo para todos os metodos (hints)
pa = t.proximo()


#crie o metodo que registre a resposta dada (no aluno)
pa.registrar_resposta(pontos = 1)


#crie o metodo que liste os alunos e pontos
t.listar()


#crie um looping que pergunte, registre e mostre as respostas até cancelar
while True :
    pa = t.proximo()
    print(f"Pergunta a {pa.nome}")
    pontos = input("Resposta correta? 1 Parcial, 2 Total, 0 Incorreta")
    pa.registrar_resposta(pontos)

    resp = input(f"Perguntar novamente? S/N")

    if resp == "N":
        print(t.listar())
        break



