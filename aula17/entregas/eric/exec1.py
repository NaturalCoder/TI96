"""
****  SEM USAR IA ****

Crie uma exceção personalizada:
1. Crie a classe IdadeInvalida herdando de Exception
2. Faça uma função que valide idades
3. Lance a exceção personalizada quando necessário
"""

class IdadeInvalida(Exception):
    mensagem = "Idade inválida"

    def __init__(self, idade):
        self.idade = idade
        super().__init__(f"{self.mensagem}: {idade}")


def validar_idade(idade):
    if idade < 0:
        raise IdadeInvalida(f"A '{idade}' não é válida.")
    
try:
    idade = int(input("Digite sua idade: "))
    validar_idade(idade)
    print("Idade válida.")
except IdadeInvalida as e:
    print(f"Erro: {e.mensagem}")
    print("Informe uma idade válida.")