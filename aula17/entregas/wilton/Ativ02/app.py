"""
****  SEM USAR IA ****

Crie uma validação de senha com exceção personalizada:
1. Crie SenhaFracaError herdando de Exception
2. Valide mínimo 8 caracteres
3. Lance a exceção se não atender
"""

class SenhaFracaSenha(Exception):

    pass

def validar_senha(minhasenha):
    if len(minhasenha) < 8:
        raise SenhaFracaSenha("Senha Fraca no minino 8 caractereres")
    print("Senha Valida!")    

def main ():
    try:

        minhasenha = input("Digitar sua senha: ")
        validar_senha(minhasenha)
    except SenhaFracaSenha as e:
        print(f"erro de senha: {e}")
    finally:
        print("Validação de senha concluída")

if __name__ == '__main__':
    main()
