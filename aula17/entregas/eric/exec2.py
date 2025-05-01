"""
****  SEM USAR IA ****

Crie uma validação de senha com exceção personalizada:
1. Crie SenhaFracaError herdando de Exception
2. Valide mínimo 8 caracteres
3. Lance a exceção se não atender
"""
class SenhaFracaError(Exception):
    mensagem = "Senha fraca, a senha deve ter no mínimo 8 caracteres"

    def __init__(self, senha):
        self.senha = senha
        super().__init__(f"{self.mensagem}: {senha}")

def validar_senha(senha):
    if len(senha) < 8:
        raise SenhaFracaError(senha)
    print("Senha válida!")

try:
    senha = input("Digite sua senha: ")
    validar_senha(senha)
except SenhaFracaError as e:
    print(f"Erro: {e.mensagem}")
    print("Informe uma senha válida.")