class IdadeInvalida(Exception):
    pass

def validar_idade(idade):
    if idade < 0:
        raise IdadeInvalida("Idade não pode ser negativa.")

try:
    validar_idade(-2)
except IdadeInvalida as erro:
    print("Erro:", erro)