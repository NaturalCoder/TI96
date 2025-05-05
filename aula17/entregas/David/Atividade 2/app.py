
class SenhaFracaError(Exception):
    def __init__(self, senha, mensagem="Parece que a senha que você digitou é um pouco fraca."):
        self.senha = senha
        self.mensagem = mensagem
        super().__init__(self.mensagem)

    def __str__(self):
        return f"A senha que você tentou usar tem apenas {len(self.senha)} caracteres. {self.mensagem} Tente usar uma senha com pelo menos 8 caracteres para maior segurança."


def validarsenha(senha):
    if len(senha) < 8:
     
        raise SenhaFracaError(senha)
    else:
        print(f"Perfeito! Sua senha tem {len(senha)} caracteres. Tudo certo por aqui!")


try:
    senha_usuario = input("Crie sua senha (pelo menos 8 caracteres): ")
    validarsenha(senha_usuario)
except SenhaFracaError as e:
    print(f"Oops! {e}")
