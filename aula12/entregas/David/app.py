from typing import List

class Aluno:
    def __init__(self, id: int, nome: str, pontos: int = 0, perguntas: int = 0):
        self.id: int = id
        self.nome: str = nome
        self.pontos: int = pontos
        self.perguntas: int = perguntas

    def registrar_resposta(self, pontos: int) -> None:
        """Registra os pontos obtidos pelo aluno e incrementa o número de perguntas."""
        self.pontos += pontos
        self.perguntas += 1

    def __repr__(self) -> str:
        return f"{self.nome}: {self.pontos} pontos, {self.perguntas} perguntas"


class Turma:
    def __init__(self, alunos: List[Aluno]):
        self.alunos: List[Aluno] = alunos
        self.indice_atual: int = -1
        self.historico: List[int] = []

    def proximo(self) -> Aluno:
        """Retorna o próximo aluno a responder, garantindo que todos sejam chamados antes de repetir."""
        if len(self.historico) == len(self.alunos):
            self.historico.clear()  # Reseta o histórico após todos serem chamados

        while True:
            self.indice_atual = (self.indice_atual + 1) % len(self.alunos)
            if self.indice_atual not in self.historico:
                self.historico.append(self.indice_atual)
                return self.alunos[self.indice_atual]

    def listar(self) -> List[str]:
        """Lista os alunos e seus respectivos pontos e perguntas."""
        return [str(aluno) for aluno in self.alunos]


# Exemplo de uso
if __name__ == "__main__":
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

    while True:
        pa = t.proximo()
        print(f"Pergunta a {pa.nome}")
        try:
            pontos = int(input("Resposta correta? 1 Parcial, 2 Total, 0 Incorreta: "))
        except ValueError:
            print("Entrada inválida. Pontos definidos como 0.")
            pontos = 0

        pa.registrar_resposta(pontos)

        resp = input("Perguntar novamente? S/N: ").strip().upper()
        if resp == "N":
            print("Resultados finais:")
            print("\n".join(t.listar()))
            break