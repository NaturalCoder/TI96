class Aluno():
    def __init__(self, id, nome, pontos = 0, perguntas = 0):
        self.id = id
        self.nome = nome
        self.pontos = pontos
        self.perguntas = perguntas
 
class Turma():
    def __init__(self, alunos):
        self.alunos = alunos
class A():
    pass

z =1

#explique:

x = 42

x = []

x = {}

x = [42]

x = ["42"]

x = "z"

x = z

x = [z]

x = [z, "z", 1]

x = A()

x = A(42)

x = Turma()

x = Turma([])

a = Aluno('João')

x = Turma([Aluno('João')])

x = Turma([Aluno('João'), z])



