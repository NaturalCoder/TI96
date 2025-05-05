"""
****  SEM USAR IA ****

Crie uma validação de senha com exceção personalizada:
1. Crie SenhaFracaError herdando de Exception
2. Valide mínimo 8 caracteres
3. Lance a exceção se não atender
"""
class SenhaFracaError(Exception):
    pass

def validar_senha(senha):
    if len(senha) < 8:
        raise SenhaFracaError("A senha deve ter no mínimo 8 caracteres.")
    else:
        print("Senha válida.")

try:
   
    senha = input("Digite a senha: ")
    validar_senha(senha)

except SenhaFracaError as erro_senha:
    print(f"Erro de senha: {erro_senha}")
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de digitar um número para a idade.")