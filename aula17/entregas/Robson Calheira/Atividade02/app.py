"""
****  SEM USAR IA ****

Crie uma validação de senha com exceção personalizada:
1. Crie SenhaFracaError herdando de Exception
2. Valide mínimo 8 caracteres
3. Lance a exceção se não atender
"""



#uso:
class SenhaFracaError(Exception):
    """Exceção personalizada para senha fraca."""
    pass

def validarsenha(senha):
    if len(senha) < 8:
        raise SenhaFracaError("A senha deve ter pelo menos 8 caracteres.")
    print("Senha válida.")


validarsenha("minhasenha")  
