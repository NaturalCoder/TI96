class SenhaFracaError(Exception):
    
    def __init__(self, mensagem="A senha deve ter pelo menos 8 caracteres."):
        super().__init__(mensagem)

def validar_senha(senha):
     if len(senha) < 8:
        raise SenhaFracaError()
try:
    senha = input("Digite sua senha: ")
    validar_senha(senha)
    print("Senha válida!")
except SenhaFracaError as e:
    print(f"Erro: {e}")