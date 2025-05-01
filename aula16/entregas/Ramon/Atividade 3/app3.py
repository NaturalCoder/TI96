"""
****  SEM USAR IA ****

Crie uma exceção personalizada:
1. Crie a classe IdadeNegativaError herdando de Exception
2. Faça uma função que valide idades positivas
3. Lance a exceção personalizada quando necessário
"""

# 1 Criação da exceção personalizada
class IdadeNegativaError(Exception):
    def __init__(self, mensagem="A idade não pode ser negativa."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

# 2 Função para validar idades positivas
def validar_idade(idade):
    if idade < 0:
        # 3 Lançamento da exceção personalizada
        raise IdadeNegativaError(f"Idade fornecida: {idade}. A idade não pode ser negativa.")
    else:
        print(f"Idade {idade} válida!")

# Teste da função
try:
    idade_usuario = int(input("Digite a idade: "))
    validar_idade(idade_usuario)
except IdadeNegativaError as e:
    print(f"Erro: {e}")
