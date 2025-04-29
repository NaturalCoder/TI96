class IdadeNegativaError(Exception):
    """Exceção lançada quando a idade fornecida é negativa."""
    pass

def validar_idade(idade):
    if idade < 0:
        
        raise IdadeNegativaError(f"Idade inválida: {idade}. A idade não pode ser negativa.")
    print(f"Idade válida: {idade} anos.")

try:
    idade_usuario = int(input("Digite sua idade: "))
    validar_idade(idade_usuario)
except IdadeNegativaError as e:
    print(f"Erro de idade: {e}")
except ValueError:
    print("Erro: Você deve digitar um número inteiro válido.")
