"""
****  SEM USAR IA ****

Crie uma exceção personalizada:
1. Crie a classe IdadeInvalida herdando de Exception
2. Faça uma função que valide idades
3. Lance a exceção personalizada quando necessário
"""



class IdadeInvalida(Exception):
    def __init__(self, idade, mensagem="Idade inválida fornecida."):
        self.idade = idade
        self.mensagem = mensagem
        super().__init__(f"{mensagem} Valor recebido: {idade}")


def validar_idade(idade):
    if not isinstance(idade, int):
        raise IdadeInvalida(idade, "A idade deve ser um número inteiro.")
    if idade < 0 or idade > 120:
        raise IdadeInvalida(idade, "A idade deve estar entre 0 e 120.")
    print(f"Idade {idade} é válida.")

try:
    idade_usuario = int(input("Digite sua idade: "))
    validar_idade(idade_usuario)
except IdadeInvalida as e:
    print(f"Erro: {e}")
