"""
****  SEM USAR IA ****

Crie uma validação de senha com exceção personalizada:
1. Crie SenhaFracaError herdando de Exception
2. Valide mínimo 8 caracteres
3. Lance a exceção se não atender
"""



#uso:
#validarsenha("minhasenha")



class SenhaFracaError(Exception):
    pass


def validar_senha(minhasenha):
    if len(minhasenha) < 8:
        
        raise SenhaFracaError(minhasenha)
    print("Senha válida!")


try:
    senha_usuario = input("Digite sua senha: ")
    validar_senha(senha_usuario)
except SenhaFracaError as e:
    print(f"Erro: {e}")
