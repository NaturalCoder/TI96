"""
****  SEM USAR IA ****

Crie uma validação de senha com exceção personalizada:
1. Crie SenhaFracaError herdando de Exception
2. Valide mínimo 8 caracteres
3. Lance a exceção se não atender
"""


class SenhaFracaError(Exception):
    def __init__(self, mensagem="A senha é fraca. Ela deve conter pelo menos 8 caracteres."):
        super().__init__(mensagem)

def validar_senha(senha):
    
    if len(senha) < 8:
        raise SenhaFracaError()
    print("Senha válida.")

try:
    senha = input("Digite sua senha: ")
    validar_senha(senha)
except SenhaFracaError as e:
    print(f"Erro: {e}")
