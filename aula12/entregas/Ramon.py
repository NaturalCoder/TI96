import random
from typing import List, Optional

class Aluno:
    def __init__(self, id: int, nome: str, pontos: int = 0, perguntas: int = 0):
        self.id = id
        self.nome = nome
        self.pontos = pontos
        self.perguntas = perguntas

    def registrar_resposta(self, pontos: int) -> None:
        self.pontos += pontos
        self.perguntas += 1

    def __str__(self) -> str:
        return f"{self.nome} - Pontos: {self.pontos}, Perguntas: {self.perguntas}"

class Turma:
    def __init__(self, alunos: List[Aluno]):
        self.alunos = alunos
        self._fila_ids = [aluno.id for aluno in alunos]
        random.shuffle(self._fila_ids)
        self._ultimo_id: Optional[int] = None

    def proximo(self) -> Aluno:
        if not self._fila_ids:
            self._fila_ids = [aluno.id for aluno in self.alunos]
            random.shuffle(self._fila_ids)
            # Garante que o próximo aluno não seja o mesmo que o último
            if self._ultimo_id is not None and self._fila_ids[0] == self._ultimo_id and len(self._fila_ids) > 1:
                self._fila_ids[0], self._fila_ids[1] = self._fila_ids[1], self._fila_ids[0]

        proximo_id = self._fila_ids.pop(0)
        self._ultimo_id = proximo_id
        return self._get_aluno_by_id(proximo_id)

    def _get_aluno_by_id(self, id: int) -> Aluno:
        for aluno in self.alunos:
            if aluno.id == id:
                return aluno
        raise ValueError(f"Aluno com id {id} não encontrado.")

    def listar(self) -> str:
        return "\n".join(str(aluno) for aluno in self.alunos)


# Exemplo de uso:
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

# Loop de perguntas
while True:
    aluno = t.proximo()
    print(f"\nPergunta para: {aluno.nome}")
    pontos = input("Resposta (0 = Incorreta, 1 = Parcial, 2 = Total): ")

    try:
        pontos_int = int(pontos)
        if pontos_int not in [0, 1, 2]:
            raise ValueError
        aluno.registrar_resposta(pontos_int)
    except ValueError:
        print("Entrada inválida. Use apenas 0, 1 ou 2.")
        continue

    continuar = input("Perguntar novamente? (S/N): ").strip().upper()
    if continuar == "N":
        print("\nResumo da turma:")
        print(t.listar())
        break
