
class IdadeInvalida(Exception):
    def __init__(self, idade, mensagem="Ops! Parece que essa idade não é válida."):
        self.idade = idade
        self.mensagem = mensagem
        super().__init__(self.mensagem)

    def __str__(self):
        return f"Você informou a idade {self.idade}. {self.mensagem} Tente novamente com uma idade entre 0 e 150 anos."


def validar_idade(idade):
    if idade < 0 or idade > 150:
    
        raise IdadeInvalida(idade)
    else:
        print(f"Idade {idade} confirmada! Tudo certo por aqui.")


try:
    idade_usuario = int(input("Por favor, digite sua idade: "))
    validar_idade(idade_usuario)
except IdadeInvalida as e:
    print(f"Erro: {e}")
