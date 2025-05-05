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
    if idade < 0 or idade > 200:
        
        raise IdadeInvalida("A idade informada não é válida")
    print(f"Idade válida: {idade} anos.")


try:
    idade_usuario = int(input("Digite sua idade: "))
    validar_idade(idade_usuario)
except IdadeInvalida as e:
    print(f"Erro: {e}")
except ValueError:
    print("Erro: Digite um número inteiro válido.")
