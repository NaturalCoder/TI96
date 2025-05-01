"""
****  SEM USAR IA ****

Crie uma exceção personalizada:
1. Crie a classe IdadeInvalida herdando de Exception
2. Faça uma função que valide idades
3. Lance a exceção personalizada quando necessário
"""

class IdadeInvalida(Exception):
    pass

def validar_idade(idade):
    if idade < 0:
        raise IdadeInvalida("Idade não pode ser negativa.")
    elif idade > 150:
        raise IdadeInvalida("Idade não pode ser maior que 150 anos.")
    else:
        print(f"Idade {idade} é válida.")

try:
    idade = int(input("Digite a idade: "))
    validar_idade(idade)
except IdadeInvalida as erro:
    print(f"Erro: {erro}")
except ValueError:
    print("Erro: Você deve digitar um número inteiro.")