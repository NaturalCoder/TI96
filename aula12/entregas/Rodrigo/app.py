import random
from typing import List, Optional
 
#teste
class Aluno:
    def __init__(self, id: int, nome: str, pontos: int = 0, perguntas: int = 0) -> None:
        self.id = id
        self.nome = nome
        self.pontos = pontos
        self.perguntas = perguntas
 
    def registrar_resposta(self, pontos: int) -> None:
        self.pontos += pontos
        self.perguntas += 1
 
 
class Turma:
    def __init__(self, alunos: List[Aluno]) -> None:
        self.alunos = alunos
        self._fila_ids: List[int] = list(range(len(alunos)))
        random.shuffle(self._fila_ids)
        self._ultimo_id: Optional[int] = None
 
    def proximo(self) -> Aluno:
        if not self._fila_ids:
            # Reinicia a fila sem repetir o último aluno imediatamente
            nova_fila = list(range(len(self.alunos)))
            if self._ultimo_id is not None and len(nova_fila) > 1:
                nova_fila.remove(self._ultimo_id)
                random.shuffle(nova_fila)
                nova_fila.insert(random.randint(1, len(nova_fila)), self._ultimo_id)
            else:
                random.shuffle(nova_fila)
            self._fila_ids = nova_fila
 
        id_proximo = self._fila_ids.pop(0)
        self._ultimo_id = id_proximo
        return self.alunos[id_proximo]
 
    def listar(self) -> str:
        resultado = "\n".join(
            f"{aluno.nome}: {aluno.pontos} pontos, {aluno.perguntas} perguntas"
            for aluno in self.alunos
        )
        return resultado
 
 
# Instanciando a turma
t = Turma([
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
])
 
# Loop principal de perguntas
while True:
    aluno = t.proximo()
    print(f"\nPergunta para: {aluno.nome}")
    entrada = input("Resposta correta? (0 = Incorreta, 1 = Parcial, 2 = Total): ")
 
    try:
        pontos = int(entrada)
        if pontos not in [0, 1, 2]:
            raise ValueError
    except ValueError:
        print("Entrada inválida. Considerando 0 pontos.")
        pontos = 0
 
    aluno.registrar_resposta(pontos)
 
    continuar = input("Deseja perguntar novamente? (S/N): ").strip().upper()
    if continuar != 'S':
        print("\nResultado Final:\n")
        print(t.listar())
        break
 
 