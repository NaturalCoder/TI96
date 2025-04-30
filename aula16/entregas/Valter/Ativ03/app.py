
"""
****  SEM USAR IA ****

Crie uma exceção personalizada:
1. Crie a classe IdadeNegativaError herdando de Exception
2. Faça uma função que valide idades positivas
3. Lance a exceção personalizada quando necessário
"""


class IdadeNegativaError(Exception):
    def __init__(self, mensagem="Idade não pode ser negativa"):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

def validar_idade(idade):
    if idade < 0:
        raise IdadeNegativaError("A idade fornecida é negativa. Insira uma idade válida.")
    else:
        print(f"A idade {idade} é válida.")

try:
    idade = int(input("Digite sua idade: "))
    validar_idade(idade)
except IdadeNegativaError as e:
    print(f"Erro: {e}")
